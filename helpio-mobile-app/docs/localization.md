# Helpio - Localization Guide

## 🌍 Languages Support

### Phase 1: Tunisia 🇹🇳
- **Primary**: Tunisian Arabic (تونسي - Dialect)
- **Secondary**: French (for professional terms)
- **Bilingual Categories**: French/Arabic labels

### Phase 2: Germany 🇩🇪
- German (Deutsch)
- English (fallback)

## 📝 Translation Files Structure

```
/localization
  ├── ar-TN.json          # Tunisian Arabic
  ├── fr-TN.json          # French (Tunisia)
  ├── de-DE.json          # German (Germany)
  └── en-US.json          # English (International)
```

## 🇹🇳 Tunisian Arabic Translations

### Common Phrases (Tunisian Dialect)

#### Greetings & Welcome
- "أهلاً بيك" - Welcome (informal)
- "مرحبا" - Hello
- "كيفك؟" - How are you?
- "بالصحّة" - You're welcome / Health to you
- "يعيّشك" - Thank you

#### App Core
- "الرئيسية" - Home
- "بحث" - Search
- "رسائل" - Messages
- "حسابي" - My Account
- "طلبات" - Requests
- "خدمات" - Services
- "مختصين" - Specialists/Providers

#### Actions
- "اطلب خدمة" - Request Service
- "شنوّا تحب؟" - What do you want?
- "اختار" - Choose
- "أكّد" - Confirm
- "ألغي" - Cancel
- "راسل" - Send Message
- "اتصل" - Call
- "زيد" - Add
- "احذف" - Delete

#### Service Request
- "شنوّا الخدمة اللي تحتاجها؟" - What service do you need?
- "وصف المشكلة" - Problem Description
- "اكتب التفاصيل..." - Write details...
- "زيد صور" - Add photos
- "الميزانية المتوقعة" - Expected budget
- "دينار" - Dinar (currency)
- "فلوس" - Money (colloquial)

#### Categories (Bilingual)
- "Plombier / سبّاك" - Plumber
- "Électricien / كهربائي" - Electrician
- "Menuisier / نجّار" - Carpenter
- "Peintre / دهّان" - Painter
- "Mécanicien / ميكانيسيان" - Mechanic
- "Coiffeur / حلّاق" - Hairdresser
- "Nettoyage / تنظيف" - Cleaning
- "Jardinier / بستاني" - Gardener
- "Maçon / بنّاي" - Mason
- "Professeur / أستاذ" - Teacher

#### Status Messages
- "قاعد ننتظر..." - Waiting...
- "تمّت" - Done/Completed
- "ملغية" - Cancelled
- "قاعد يخدم" - Working/In Progress
- "مقبول" - Accepted
- "مرفوض" - Rejected

#### Marketing Copy
- "برشا خيارات" - Many options
- "فريق محترف" - Professional team
- "خدمة سريعة" - Fast service
- "أسعار معقولة" - Reasonable prices
- "ضمان الجودة" - Quality guarantee
- "متاح 24/7" - Available 24/7

### User Interface Labels

#### Navigation
```json
{
  "home": "الرئيسية",
  "search": "بحث",
  "post": "اطلب",
  "messages": "رسائل",
  "profile": "حسابي",
  "dashboard": "لوحة التحكم",
  "requests": "الطلبات",
  "settings": "الإعدادات"
}
```

#### Form Fields
```json
{
  "name": "الاسم",
  "phone": "رقم التليفون",
  "email": "البريد الإلكتروني",
  "password": "كلمة المرور",
  "location": "الموقع",
  "description": "الوصف",
  "category": "الفئة",
  "price": "السعر",
  "date": "التاريخ",
  "time": "الوقت"
}
```

#### Buttons
```json
{
  "continue": "كمّل",
  "next": "التالي",
  "previous": "الرجوع",
  "submit": "إرسال",
  "confirm": "تأكيد",
  "cancel": "إلغاء",
  "save": "حفظ",
  "edit": "تعديل",
  "delete": "حذف",
  "send": "إرسال",
  "call": "اتصل",
  "message": "راسل"
}
```

#### Notifications
```json
{
  "new_offer": "عندك عرض جديد من {provider}",
  "new_message": "{provider} بعثلك رسالة",
  "booking_confirmed": "الحجز متاعك تأكّد مع {provider}",
  "service_starting": "{provider} قاعد يجي",
  "payment_received": "استلمت {amount} دينار",
  "review_request": "قيّم الخدمة متاع {provider}"
}
```

## 🇫🇷 French Translations (Tunisia Context)

### Professional Services
```json
{
  "plumber": "Plombier",
  "electrician": "Électricien",
  "carpenter": "Menuisier",
  "painter": "Peintre",
  "mechanic": "Mécanicien",
  "hairdresser": "Coiffeur",
  "cleaning": "Nettoyage",
  "teacher": "Professeur"
}
```

## 🇩🇪 German Translations (Phase 2)

### Core App
```json
{
  "home": "Startseite",
  "search": "Suchen",
  "post_request": "Anfrage stellen",
  "messages": "Nachrichten",
  "profile": "Profil",
  "request_service": "Service anfragen",
  "find_provider": "Dienstleister finden"
}
```

### Service Categories
```json
{
  "plumber": "Klempner",
  "electrician": "Elektriker",
  "carpenter": "Tischler",
  "painter": "Maler",
  "mechanic": "Mechaniker",
  "hairdresser": "Friseur",
  "cleaning": "Reinigung",
  "gardener": "Gärtner"
}
```

## 📱 Implementation Notes

### RTL Support
- Tunisian Arabic requires **Right-to-Left (RTL)** layout
- Flip navigation, alignment, and gestures
- Keep numbers and prices in LTR format
- Icons should mirror appropriately

### Mixed Content
When mixing Arabic and French:
```
"Plombier / سبّاك"  ✓ Correct
"سبّاك / Plombier"  ✗ Less natural for Tunisia
```

### Font Recommendations
- **Arabic**: Tajawal, Cairo, Amiri, Lateef
- **Latin**: Inter, Roboto, SF Pro
- Ensure proper Arabic character support

### Number Formatting
- Tunisia: `123 456.78 DT` (spaces as thousands separator)
- Germany: `123.456,78 €` (period as thousands, comma as decimal)
- Keep numbers in Western-Arabic numerals (1,2,3...) not Eastern (١,٢,٣...)

### Cultural Considerations

#### Tunisia 🇹🇳
- Informal, friendly tone in dialect
- Mix French for professional/formal terms
- Use colloquial expressions
- Emphasize trust and community

#### Germany 🇩🇪
- Formal tone (Sie, not du)
- Professional language
- Emphasize efficiency and reliability
- GDPR compliance messaging

## 🔄 Translation Workflow

1. **English (Base)** → Master copy
2. **Tunisian Arabic** → Primary market
3. **French (TN)** → Secondary support
4. **German** → International expansion
5. **Community Translation** → User contributions

## ✅ Quality Checklist

- [ ] All strings extracted from code
- [ ] Native speaker review
- [ ] Cultural appropriateness check
- [ ] Character encoding tested (UTF-8)
- [ ] RTL layout verified
- [ ] Placeholder text translated
- [ ] Error messages localized
- [ ] Date/time formats adapted
- [ ] Currency symbols correct
- [ ] Legal terms reviewed

---

**Translation Partner**: Ideally work with Tunisian native speakers who understand both dialect and formal Arabic, plus French usage in Tunisia.
