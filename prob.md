# UniPlace 

**INF 23 B, Semester 4**  
Prof. Dr. Alexander Auch  
30.03.2025  

**Dennis Pinder** (9930287)
**Lea Liedtke** (3260935)  
**Recep Özmen** (4302297)  
**Sven Niggemann** (8466840)  

## Einleitung

Uniplace ist ein innovativer, webbasierter Marktplatz, der es Nutzern ermöglicht, Artikel anzubieten, zu suchen und zu verwalten. Die Plattform richtet sich insbesondere an Studierende und andere Nutzergruppen, die auf einfache Weise Waren und Dienstleistungen austauschen möchten. Ein zentrales Feature von Uniplace ist die Möglichkeit, als Kunde ein eigenes Konto zu erstellen, sich einzuloggen und auf alle Funktionen des Marktplatzes zuzugreifen.

Die Benutzer können gezielt nach Produkten suchen und sich die Kontaktdaten der jeweiligen Anzeigenersteller direkt in der Produktbeschreibung anzeigen lassen. Zudem haben sie die Möglichkeit, eigene Artikel zum Verkauf oder Tausch anzubieten, bestehende Angebote zu bearbeiten oder zu löschen.

Ein herausragendes Merkmal von Uniplace ist die Unterstützung von sieben verschiedenen Währungen (EUR, USD, GBP, JPY, KRW, CNY, MXN), sodass internationale Transaktionen vereinfacht werden. Durch diese Funktion wird die Plattform für eine größere Nutzerbasis attraktiv, insbesondere für Personen, die grenzüberschreitend handeln oder in unterschiedlichen Währungen bezahlen möchten.

Neben den grundlegenden Marktplatzfunktionen setzt Uniplace auf eine benutzerfreundliche Oberfläche und ein intuitives Design, um eine nahtlose User Experience zu gewährleisten. Die Plattform bietet zudem Mechanismen zur Sicherstellung von Datenschutz und Sicherheit der Nutzerinformationen.

Im Rahmen dieses Projekts wurden verschiedene technische Aspekte realisiert, darunter die Einrichtung der Datenbank, die Integration externer APIs und die Automatisierung von Wechselkurs-Updates. Diese Dokumentation beschreibt die einzelnen Schritte der Entwicklung und Implementierung der zentralen Funktionen von Uniplace.

## Projektorganisation
|Dennis Pinder|Lea Liedtke|Recep Özmen|Sven Niggemann|
|||||||
|||||||

## Systemarchitektur

## Backend & API

## Datenbank 

## Frontend

### Übersicht

Das Frontend von UniPlace wurde mit Vue.js entwickelt und bietet eine benutzerfreundliche Oberfläche für den digitalen Marktplatz. Die Anwendung ermöglicht Benutzern das Erstellen eines Kontos, das Einstellen von Produkten zum Verkauf, den Kauf von Produkten und die Verwaltung ihrer eigenen Angebote.

### Technologie-Stack

- **Framework:** Vue.js 3
- **Router:** Vue Router
- **State Management:** Vue Event Bus
- **Styling:** CSS mit konsistenten Klassen (ähnlich zu Tailwind CSS-Konzepten)
- **HTTP-Requests:** REST.js (interne API-Wrapper-Bibliothek)
- **Verschlüsselung:** CryptoJS (für sichere Passwortverarbeitung)

### Komponenten-Struktur

#### Hauptkomponenten

1. **SignUp.vue** - Benutzerregistrierung
2. **ArticleView.vue** - Anzeige aller verfügbaren Produkte
3. **AddArticleView.vue** - Hinzufügen neuer Produkte
4. **MyArticlesView.vue** - Verwaltung eigener Produkte
5. **Currency.vue** - Währungsauswahl und -umrechnung
6. **AboutUs.vue** - Informationsseite über UniPlace
7. **Footer.vue** - Fußzeile mit Navigation und Copyright

### Design-System

UniPlace verwendet ein konsistentes Designsystem mit:

- Gradienthintergründen
- Einheitlichem Button-Styling
- Responsivem Layout
- Modalen Dialogen für Detailansichten
- Feedback-Meldungen für Benutzeraktionen

#### CSS-Klassen

```css
/* Dunklerer Hintergrund */
.bg-dark {
  background: linear-gradient(to bottom right, #1a202c, #2d3748, #4a5568);
  color: white;
}

/* Spezieller Farbverlaufshintergrund */
.bg-special {
  background: linear-gradient(to left, #5cbbca, #c59bec);
  color: white;
  width: 100%;
  padding: 1rem;
}
```

### Kernfunktionen und Implementierungsbeispiele

#### 1. Benutzerregistrierung (SignUp.vue)

```javascript
const signUp = () => {
  if(!checkValues()){
    hashedPassword.value = CryptoJS.SHA256(username.value+password.value).toString(CryptoJS.enc.Hex);
    sendSignUpData()
  } else {
    errormessage.value = "Please input your data";
    openPopup();
  }
}
```

#### 2. Produktanzeige (ArticleView.vue)

```javascript
// Produktdetails anzeigen
function getDetails(product){
    certainProduct = product;
    isPopupVisible.value = true;
}
```

```html
<!-- Produktliste -->
<div class="product-item" v-for="product in products">
    <p class="product-field"><strong>Produkt:</strong> {{ product.title }}</p>
    <p class="product-field"><strong>Preis:</strong> {{ (product.price * currencyRate).toFixed(2) }} {{currencySymbol}}</p>
    <button class="detailButton" @click="getDetails(product)">Details</button>
</div>
```


