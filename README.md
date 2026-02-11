<div align="center">

# 🚀 Tech Event Platform

A modern, feature-rich event management platform built with React for hosting and managing tech events.

[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?style=for-the-badge&logo=react&logoColor=white)](https://reactjs.org/)
[![React Router](https://img.shields.io/badge/React_Router-6.8.1-CA4245?style=for-the-badge&logo=react-router&logoColor=white)](https://reactrouter.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

[Demo](#) • [Features](#features) • [Getting Started](#getting-started) • [Documentation](#documentation)

</div>

---

## ✨ Features

### 🎯 Core Functionality
- **📅 Event Management** - Browse, search, and explore tech events with detailed information
- **🏆 Leaderboard System** - Track participant rankings and achievements
- **📝 Event Registration** - Seamless registration process for events
- **📊 Individual Event Pages** - Dedicated pages with comprehensive event details
- **📱 Responsive Design** - Optimized for all devices and screen sizes

### 🎨 User Experience
- **🌐 Smooth Navigation** - React Router integration with hash-link support
- **⚡ Loading States** - Custom loading animations for better UX
- **🎭 Modal Popups** - Interactive popups for important announcements
- **📞 Contact System** - Direct communication channel with organizers
- **🤝 Sponsor Showcase** - Dedicated section for event sponsors

### 🔧 Technical Features
- **📈 Google Analytics** - Built-in analytics tracking
- **🎨 FontAwesome Icons** - Rich icon library integration
- **♿ Accessibility** - ARIA compliant components
- **🔄 React Icons** - Modern iconography support
- **📜 Scroll Management** - Smooth scrolling with react-scroll

---

## 🚀 Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chilkotiKartik/tech.git
   cd tech
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

4. **Open your browser**
   
   Navigate to [http://localhost:3000](http://localhost:3000)

---

## 📖 Available Scripts

### `npm start`
Runs the app in development mode at [http://localhost:3000](http://localhost:3000)
- Hot reload on file changes
- Displays lint errors in console

### `npm test`
Launches the test runner in interactive watch mode

### `npm run build`
Creates an optimized production build in the `build` folder
- Minified and optimized for best performance
- Filenames include content hashes
- Ready for deployment

### `npm run eject`
**⚠️ Warning: This is a one-way operation!**

Ejects from Create React App to gain full control over configuration

---

## 🏗️ Project Structure

```
tech/
├── public/              # Static files
├── src/
│   ├── assets/         # Images, fonts, and other assets
│   ├── components/     # Reusable React components
│   │   ├── Navbar/
│   │   ├── Footer/
│   │   ├── MainEvents/
│   │   ├── SingleEventPage/
│   │   ├── ContactUs/
│   │   ├── Sponser/
│   │   ├── Hidden/
│   │   └── common/     # Shared components
│   │       ├── Button/
│   │       ├── Register/
│   │       ├── Loading/
│   │       └── Popup/
│   ├── pages/          # Page components
│   │   ├── Homepage.jsx
│   │   ├── AboutPage.jsx
│   │   └── Leaderboard.jsx
│   ├── App.jsx         # Main app component
│   ├── index.js        # Entry point
│   └── index.css       # Global styles
├── package.json
└── README.md
```

---

## 🛠️ Built With

### Core Technologies
- **React** (18.2.0) - UI library
- **React Router DOM** (6.8.1) - Client-side routing
- **React Scripts** (5.0.1) - Build tooling

### UI & Icons
- **FontAwesome** - Professional icon library
- **React Icons** (4.7.1) - Popular icon sets
- **React Scroll** (1.8.9) - Smooth scrolling

### Analytics & Navigation
- **React GA** (3.3.1) - Google Analytics integration
- **React Router Hash Link** (2.4.3) - Hash-based navigation
- **Swup** (3.0.4) - Page transitions (configurable)

---

## 🌟 Key Features Explained

### Event System
The platform provides a comprehensive event management system:
- Main events listing page
- Individual event detail pages with dynamic routing
- Event registration functionality

### Leaderboard
Track and display participant rankings:
- Real-time leaderboard updates
- Multiple leaderboard views

### Navigation
Seamless user experience with:
- Persistent navbar across all pages
- Hash-link navigation support
- Automatic scroll-to-top on route changes

### Analytics
Built-in Google Analytics integration for:
- Page view tracking
- User behavior analysis
- Event conversion metrics

---

## 📱 Routes

| Route | Description |
|-------|-------------|
| `/` | Homepage with featured events |
| `/events` | Complete events listing |
| `/events/:eventId` | Individual event details |
| `/leaderboard` | Rankings and scores |
| `/about` | About the platform |
| `/register` | Event registration |
| `/contact` | Contact form |

---

## 🎨 Customization

### Updating Theme Colors
Edit color variables in `src/index.css` or component-specific styles

### Adding New Events
Events can be managed through the events components in `src/components/MainEvents/`

### Modifying Analytics
Update the tracking ID in `src/App.jsx`:
```javascript
const TRACKING_ID = "YOUR-TRACKING-ID";
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Create React App](https://create-react-app.dev/)
- Icons by [FontAwesome](https://fontawesome.com/) and [React Icons](https://react-icons.github.io/react-icons/)
- Analytics by [Google Analytics](https://analytics.google.com/)

---

## 📞 Contact & Support

For questions, suggestions, or support:
- **Repository**: [chilkotiKartik/tech](https://github.com/chilkotiKartik/tech)
- **Issues**: [GitHub Issues](https://github.com/chilkotiKartik/tech/issues)

---

<div align="center">

**Made By Kartik Chilkoti for the tech community**

⭐ Star this repo if you find it helpful!

</div>
