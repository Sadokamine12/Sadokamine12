# Helpio - User Flows

## 🔄 Core User Journeys

### Client Journey: Request a Service

```
1. Open App
   ↓
2. See Home Screen
   - Browse categories
   - View top providers
   - See recent requests
   ↓
3. Post Service Request
   - Select category
   - Describe problem
   - Upload photos (optional)
   - Set budget
   - Add location
   - Choose urgency
   ↓
4. Receive Offers
   - Get notifications
   - View provider quotes
   - Compare prices & ratings
   - Read provider profiles
   ↓
5. Select Provider
   - Review portfolio
   - Check availability
   - Chat with provider
   - Confirm booking
   ↓
6. Service Completion
   - Track provider arrival
   - Confirm work done
   - Make payment
   - Rate & review
```

### Provider Journey: Offer a Service

```
1. Open App
   ↓
2. Dashboard
   - View new requests
   - Check bookings
   - Monitor earnings
   ↓
3. Browse Requests
   - Filter by category
   - Check location
   - View request details
   ↓
4. Submit Quote
   - Set price
   - Propose timeline
   - Add message
   - Send offer
   ↓
5. Get Accepted
   - Receive notification
   - Chat with client
   - Confirm details
   ↓
6. Complete Service
   - Navigate to location
   - Perform work
   - Mark as complete
   - Receive payment
   - Get review
```

## 📱 Screen Flows

### Onboarding Flow
```
Splash Screen
   ↓
Welcome Slides (3 slides)
   ↓
Choose User Type
   ├── Client → Client Registration
   └── Provider → Provider Registration
         ↓
Email/Phone Verification
   ↓
Profile Setup
   ↓
Home Screen
```

### Booking Flow (Client)
```
Home
   ↓
Post Request
   ├── Quick Post (Fast form)
   └── Detailed Post (Step-by-step)
         ↓
Request Posted
   ↓
Receive Offers
   ↓
View Provider Profile
   ↓
Chat with Provider
   ↓
Confirm Booking
   ↓
Payment
   ↓
Service Tracking
   ↓
Complete & Review
```

### Quote Submission Flow (Provider)
```
Dashboard
   ↓
Browse Requests
   ↓
View Request Details
   ↓
Submit Quote
   ├── Standard Quote
   └── Custom Quote
         ↓
Wait for Response
   ↓
If Accepted →
   ├── Confirm Booking
   ├── Chat with Client
   └── Schedule Service
```

## 🎯 Key Interactions

### Search & Discovery
- **Browse by Category**: Quick access to service types
- **Search Bar**: Text search with suggestions
- **Filters**: Location, price range, rating, availability
- **Sort Options**: Distance, rating, price, reviews

### Communication
- **In-app Chat**: Real-time messaging
- **Push Notifications**: Offers, messages, reminders
- **Call Button**: Direct phone call to provider
- **Video Call**: For consultations (future)

### Trust & Safety
- **Verification Badges**: ID verified providers
- **Ratings & Reviews**: Star ratings and written reviews
- **Portfolio**: Photos of previous work
- **Insurance Info**: Coverage details
- **Report System**: Flag inappropriate behavior

### Payment Flow
```
Service Complete
   ↓
Review Order Summary
   ├── Service details
   ├── Price breakdown
   └── Provider info
         ↓
Choose Payment Method
   ├── Credit/Debit Card
   ├── Cash
   └── Wallet Balance
         ↓
Process Payment
   ↓
Payment Success
   ↓
Download Receipt
```

## 🔐 Authentication Flows

### Registration (Client)
```
1. Enter phone number
2. Verify OTP
3. Set password
4. Enter name
5. Add profile photo (optional)
6. Set location
7. Complete!
```

### Registration (Provider)
```
1. Enter phone number
2. Verify OTP
3. Set password
4. Enter business details
   - Name
   - Categories/Services
   - Experience
   - Location coverage
5. Upload documents
   - ID card
   - Professional certifications
   - Business license (if applicable)
6. Set pricing
7. Add portfolio photos
8. Verification pending
9. Approval notification
10. Complete!
```

### Login
```
1. Enter phone/email
2. Enter password
   OR
   Biometric (Face ID/Fingerprint)
3. Login successful
```

## 📊 Navigation Structure

### Bottom Tab Navigation

**Client View:**
```
🏠 Home
🔍 Search
➕ Post (Center button)
💬 Messages
👤 Profile
```

**Provider View:**
```
🏠 Dashboard
📋 Requests
➕ Quick Quote (Center button)
💬 Messages
👤 Profile
```

## 🎨 Interaction Patterns

### Gestures
- **Pull to Refresh**: Update lists
- **Swipe Right**: Go back
- **Swipe Left on Card**: Quick actions (delete, archive)
- **Long Press**: Show options menu
- **Double Tap**: Like/favorite

### Animations
- **Screen Transitions**: Slide in from right
- **Card Reveal**: Fade and slide up
- **Button Press**: Scale and color change
- **Loading**: Skeleton screens
- **Success**: Checkmark animation

### Notifications
- **New Offer**: "You have a new offer from [Provider]"
- **Message**: "[Provider] sent you a message"
- **Booking Confirmed**: "Your booking with [Provider] is confirmed"
- **Service Starting**: "[Provider] is on the way"
- **Payment Received**: "Payment of [Amount] received"
- **Review Request**: "Rate your experience with [Provider]"

## 📍 Location Features

### For Clients
- Auto-detect current location
- Save multiple addresses (Home, Work)
- Set service location on map
- View nearby providers

### For Providers
- Set service coverage area
- View distance to client
- Navigation to job location
- Track travel time

---

**Note**: All flows are designed to be simple, intuitive, and mobile-first. Each step should take minimal effort and provide clear feedback to the user.
