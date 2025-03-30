# UniPlace

## INF 23 B, Semester 4

## 30.03.2025




## Frontend-Dokumentation

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

/* Titel mit Farbverlauf */
.title {
  font-size: 2rem;
  font-weight: bold;
  background: linear-gradient(to right, #22d3ee, #9333ea);
  -webkit-background-clip: text;
  color: transparent;
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

#### 3. Währungsumrechnung (Currency.vue)

```javascript
async function updateCurrencyRate() {
    try {
        if (selectedCurrency.value !== "eur") {
            const currencyRate = await fetchCurrencyRate(selectedCurrency.value);
            setCurrencyRate(currencyRate);
        } else {
            setCurrencyRate(1);
        }
    } catch (error) {
        console.error("Fehler beim Laden der Währungsdaten:", error);
    }
}
```

#### 4. Produkte verwalten (MyArticlesView.vue)

```javascript
const deleteProduct = (id) => {
    products.value = products.value.filter(product => product.id !== id);
    deleteArticle(id);
    closePopup();
};
```

### Responsive Design

Das Frontend ist vollständig responsiv gestaltet:

```css
/* Beispiel aus AboutUs.vue */
.section div {
    padding: 1rem;
    text-align: center;
}

/* Beispiel aus Currency.vue */
.flag-image {
    width: 40%;
    height: auto;
    display: block;
    margin: 1rem auto;
}
```

### Popup-Benachrichtigungen

Für Benutzerrückmeldungen werden temporäre Popup-Nachrichten verwendet:

```javascript
function openPopup(){
  isPopupVisible.value = true;
  
  setTimeout(() => {
    isPopupVisible.value = false;
  }, 2000);
};
```

```css
.popup {
  margin-top: 70px;
  margin-left: 45%;
  width: 10%;
  height: auto;
  position: fixed;
  border-radius: 10px;
  z-index: 400;
  text-align: center;
}

.errorMessage {
  color: red;
  text-align: center;
}

.successMessage {
  color: lightgreen;
  text-align: center;
}
```

### API-Integration

Alle Backend-Operationen werden über die REST.js-Bibliothek abgewickelt:

```javascript
// Beispiel aus AddArticleView.vue
const submitArticle = () => {
    if(checkProductForm()){
        successmessage.value = "Articlecreation was a success"
        isSuccessVisible.value = true

        setTimeout(() => {
            isSuccessVisible.value = false;
        }, 2000);

        createNewArticle(productForm.value.title, price, productForm.value.count, productForm.value.description);
    }
}
```
