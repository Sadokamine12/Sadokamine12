# Helpio - Technical Specification

## 🏗️ Architecture Overview

### System Architecture
```
┌─────────────────────────────────────┐
│         Mobile Apps                  │
│  ┌──────────┐    ┌──────────┐       │
│  │   iOS    │    │  Android │       │
│  └────┬─────┘    └─────┬────┘       │
└───────┼──────────────┼───────────────┘
        │              │
        └──────┬───────┘
               │ REST API / WebSocket
        ┌──────▼──────────────────┐
        │    API Gateway          │
        │   (Load Balancer)       │
        └──────┬──────────────────┘
               │
    ┌──────────┼───────────┐
    │          │           │
┌───▼───┐  ┌──▼──┐   ┌───▼────┐
│  Auth │  │ API │   │Realtime│
│Service│  │ App │   │Service │
└───┬───┘  └──┬──┘   └───┬────┘
    │         │          │
    └────┬────┴────┬─────┘
         │         │
    ┌────▼─────────▼─────┐
    │    PostgreSQL      │
    │    (Primary DB)    │
    └────────────────────┘
         │         │
    ┌────▼───┐ ┌──▼─────┐
    │ Redis  │ │   S3   │
    │ Cache  │ │ Files  │
    └────────┘ └────────┘
```

## 📱 Mobile App Stack

### Recommended: React Native

#### Dependencies
```json
{
  "dependencies": {
    "react-native": "^0.73.0",
    "react-navigation": "^6.1.0",
    "@react-navigation/native-stack": "^6.9.0",
    "@react-navigation/bottom-tabs": "^6.5.0",
    "react-native-maps": "^1.10.0",
    "react-native-geolocation-service": "^5.3.0",
    "react-native-firebase": "^18.0.0",
    "axios": "^1.6.0",
    "socket.io-client": "^4.6.0",
    "react-native-image-picker": "^7.0.0",
    "react-native-i18n": "^2.0.15",
    "react-native-vector-icons": "^10.0.0",
    "react-native-ratings": "^8.1.0",
    "stripe-react-native": "^0.35.0"
  }
}
```

### Alternative: Flutter

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^2.24.0
  firebase_auth: ^4.15.0
  cloud_firestore: ^4.13.0
  google_maps_flutter: ^2.5.0
  geolocator: ^10.1.0
  image_picker: ^1.0.0
  flutter_stripe: ^10.0.0
  socket_io_client: ^2.0.0
  provider: ^6.1.0
```

## 🔧 Backend Stack

### API Server
- **Framework**: Node.js + Express.js
- **Language**: TypeScript
- **Authentication**: JWT + Refresh Tokens
- **Real-time**: Socket.io / WebSockets

### Database
```
PostgreSQL 15+
├── Users Table
├── Providers Table
├── Requests Table
├── Offers Table
├── Bookings Table
├── Reviews Table
├── Categories Table
├── Messages Table
└── Transactions Table
```

### Caching Layer
- **Redis**: Session storage, rate limiting, caching
- **Use Cases**: 
  - API response caching
  - Real-time analytics
  - Queue management

### File Storage
- **AWS S3** (or compatible)
  - Profile photos
  - Service photos
  - Portfolio images
  - Document uploads
  - Chat media

## 📊 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    avatar_url VARCHAR(500),
    user_type ENUM('client', 'provider') NOT NULL,
    location GEOGRAPHY(POINT),
    city VARCHAR(100),
    language VARCHAR(10) DEFAULT 'ar-TN',
    is_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Providers Table
```sql
CREATE TABLE providers (
    id UUID PRIMARY KEY REFERENCES users(id),
    business_name VARCHAR(200),
    categories TEXT[], -- Array of category IDs
    bio TEXT,
    experience_years INTEGER,
    hourly_rate DECIMAL(10,2),
    service_radius INTEGER, -- in kilometers
    portfolio_urls TEXT[],
    certifications TEXT[],
    average_rating DECIMAL(3,2) DEFAULT 0,
    total_reviews INTEGER DEFAULT 0,
    total_jobs INTEGER DEFAULT 0,
    is_verified BOOLEAN DEFAULT FALSE,
    verification_documents JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Service Requests Table
```sql
CREATE TABLE service_requests (
    id UUID PRIMARY KEY,
    client_id UUID REFERENCES users(id),
    category_id UUID REFERENCES categories(id),
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    photos TEXT[],
    location GEOGRAPHY(POINT) NOT NULL,
    address TEXT,
    budget_min DECIMAL(10,2),
    budget_max DECIMAL(10,2),
    urgency ENUM('low', 'medium', 'high', 'emergency'),
    status ENUM('open', 'in_progress', 'completed', 'cancelled'),
    preferred_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Offers Table
```sql
CREATE TABLE offers (
    id UUID PRIMARY KEY,
    request_id UUID REFERENCES service_requests(id),
    provider_id UUID REFERENCES providers(id),
    price DECIMAL(10,2) NOT NULL,
    estimated_duration INTEGER, -- in minutes
    message TEXT,
    status ENUM('pending', 'accepted', 'rejected', 'withdrawn'),
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(request_id, provider_id)
);
```

### Bookings Table
```sql
CREATE TABLE bookings (
    id UUID PRIMARY KEY,
    request_id UUID REFERENCES service_requests(id),
    client_id UUID REFERENCES users(id),
    provider_id UUID REFERENCES providers(id),
    offer_id UUID REFERENCES offers(id),
    scheduled_date TIMESTAMP NOT NULL,
    actual_start TIMESTAMP,
    actual_end TIMESTAMP,
    final_price DECIMAL(10,2) NOT NULL,
    status ENUM('confirmed', 'in_progress', 'completed', 'cancelled'),
    payment_status ENUM('pending', 'paid', 'refunded'),
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Reviews Table
```sql
CREATE TABLE reviews (
    id UUID PRIMARY KEY,
    booking_id UUID REFERENCES bookings(id),
    reviewer_id UUID REFERENCES users(id),
    reviewee_id UUID REFERENCES users(id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    response TEXT, -- Provider can respond
    is_visible BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 🔐 Security

### Authentication Flow
```
1. User enters phone number
2. Send OTP via SMS (Twilio)
3. Verify OTP
4. Generate JWT access token (15 min expiry)
5. Generate refresh token (30 days expiry)
6. Store refresh token in secure database
7. Return tokens to client
8. Client stores in secure storage (Keychain/Keystore)
```

### Authorization
- **JWT Claims**: user_id, user_type, roles
- **Middleware**: Verify token on protected routes
- **Rate Limiting**: Prevent abuse (Redis-based)

### Data Protection
- **Encryption at Rest**: Database encryption
- **Encryption in Transit**: TLS 1.3
- **PII Protection**: Hash sensitive data
- **GDPR Compliance**: Data export, deletion rights

## 🔔 Push Notifications

### Firebase Cloud Messaging (FCM)
```javascript
// Notification Types
{
  "NEW_OFFER": "New offer received",
  "OFFER_ACCEPTED": "Your offer was accepted",
  "MESSAGE": "New message",
  "BOOKING_CONFIRMED": "Booking confirmed",
  "SERVICE_STARTING": "Provider on the way",
  "SERVICE_COMPLETED": "Service completed",
  "PAYMENT_RECEIVED": "Payment received",
  "REVIEW_REQUEST": "Please rate your service"
}
```

## 💳 Payment Integration

### Stripe (International)
```javascript
const payment = await stripe.paymentIntents.create({
  amount: 5000, // in millimes
  currency: 'tnd',
  payment_method_types: ['card'],
  metadata: {
    booking_id: 'xxx',
    provider_id: 'yyy'
  }
});
```

### Commission Structure
- Platform fee: 15% of transaction
- Provider receives: 85%
- Payout schedule: Weekly
- Minimum payout: 50 TND

## 📍 Maps & Location

### Google Maps API
```javascript
// Services needed:
- Maps SDK (iOS/Android)
- Places API
- Directions API
- Geocoding API
- Distance Matrix API
```

### Location Features
- Auto-detect user location
- Search places
- Calculate distance
- Navigation to service location
- Geofencing for service areas

## 📊 Analytics

### Firebase Analytics
```javascript
// Events to track:
- screen_view
- sign_up
- post_request
- submit_offer
- booking_confirmed
- payment_completed
- review_submitted
```

### Business Metrics
- User acquisition cost
- Lifetime value
- Transaction volume
- Average order value
- Provider utilization rate
- Client retention rate

## 🚀 Performance

### Optimization Strategies
- **Image Optimization**: Compress, lazy load, CDN
- **API Caching**: Redis for frequently accessed data
- **Database Indexing**: On commonly queried fields
- **Code Splitting**: Lazy load screens
- **Bundle Size**: Keep under 30MB

### Monitoring
- **Sentry**: Error tracking
- **New Relic**: Performance monitoring
- **Firebase Performance**: App performance

## 🧪 Testing

### Mobile App
```javascript
// Testing stack:
- Jest (Unit tests)
- React Native Testing Library
- Detox (E2E tests)
- Appium (Cross-platform E2E)
```

### Backend
```javascript
// Testing stack:
- Jest (Unit tests)
- Supertest (API tests)
- Artillery (Load testing)
```

### Test Coverage Target
- Unit tests: >80%
- Integration tests: >70%
- E2E critical paths: 100%

## 📦 Deployment

### Mobile Apps
```
iOS:
  - TestFlight (Beta)
  - App Store (Production)
  
Android:
  - Internal Testing
  - Closed Beta
  - Google Play Store
```

### Backend
```
Infrastructure:
  - AWS / DigitalOcean / Heroku
  - Docker containers
  - Kubernetes (if scaling)
  - CI/CD: GitHub Actions
```

### Environment Strategy
- Development
- Staging
- Production

## 🔄 CI/CD Pipeline

```yaml
# GitHub Actions workflow
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    - Run linter
    - Run unit tests
    - Run integration tests
    
  build:
    - Build Docker image
    - Push to registry
    
  deploy:
    - Deploy to staging
    - Run smoke tests
    - Deploy to production
```

## 📱 App Store Requirements

### iOS App Store
- Privacy policy URL
- Terms of service
- App preview video
- Screenshots (all devices)
- App description (Arabic + French)
- Keywords
- Age rating: 4+

### Google Play Store
- Privacy policy
- Screenshots (phone + tablet)
- Feature graphic
- App description
- Content rating
- Target audience

## 🌐 Internationalization (i18n)

### Implementation
```javascript
import i18n from 'i18next';

i18n.init({
  lng: 'ar-TN',
  fallbackLng: 'en',
  resources: {
    'ar-TN': require('./locales/ar-TN.json'),
    'fr-TN': require('./locales/fr-TN.json'),
    'de-DE': require('./locales/de-DE.json'),
  }
});
```

### RTL Support
```javascript
import { I18nManager } from 'react-native';

if (language === 'ar-TN') {
  I18nManager.forceRTL(true);
}
```

---

## 📝 Development Phases

### Phase 1: MVP (3-4 months)
- User registration/authentication
- Basic profiles
- Post requests
- Browse & search
- Offers system
- Basic chat
- Payment integration
- Reviews

### Phase 2: Enhancement (2-3 months)
- Advanced search/filters
- Real-time chat
- Push notifications
- Analytics dashboard
- Portfolio management
- Subscription plans

### Phase 3: Scale (Ongoing)
- German localization
- Video consultations
- AI matching
- Automated scheduling
- Advanced analytics
- Loyalty programs

---

**Tech Stack Summary**: React Native + Node.js + PostgreSQL + Redis + AWS S3 + Firebase + Stripe
