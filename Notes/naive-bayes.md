# 🔍 Naive Bayes Algoritması

## 📌 Naive Bayes Nedir?

Naive Bayes, olasılıksal bir **sınıflandırma algoritmasıdır**.

**Genellikle kullanıldığı alanlar:**
- Metin sınıflandırma  
- Spam filtreleme  
- Duygu analizi

**Naive Varsayım:**  
Özelliklerin (örneğin kelimeler) birbirinden **bağımsız** olduğu varsayılır.

---

## ⚙️ Temel Formüller

### 📐 Bayes Teoremi

$$
P(Y \mid x_1, \dots, x_n) = \frac{P(Y) \cdot \prod_{i=1}^n P(x_i \mid Y)}{P(x_1, \dots, x_n)}
$$

> Gözlemlenen verilere göre Y sınıfının olasılığını verir.

### 📐 Naive Bayes Formülü

$$
P(Y|x_1, ..., x_n) \propto P(Y) \prod_{i=1}^{n} P(x_i|Y)
$$

> Özelliklerin birbirinden bağımsız olduğu varsayımıyla sadeleşir.

---

## 🚫 Model Ne Öğrenmez?

⚠️ Naive Bayes şunları **öğrenmez**:
- Hangi özellikler daha belirleyici?
- Özellikler arasında etkileşim var mı?

Yalnızca **koşullu olasılıklara** bakar.

---

## ✅ Avantajlar

- Hızlı ve basit  
- Az veriyle bile etkili  
- Yüksek boyutlu verilerle iyi çalışır  
- Overfitting'e karşı dayanıklı  

## ❌ Dezavantajlar

- Özellik bağımsızlığı varsayımı çoğu zaman geçersiz  
- Özellik önemi öğrenilemez  
- Sürekli veride dağılımın **normal (Gaussian)** olduğu varsayılır  

---

## 📚 Generative vs Discriminative

### 🔁 Generative (Naive Bayes)
- Her sınıf için verinin oluşumunu modellemeye çalışır  
- **P(X|Y)** ve **P(Y)** öğrenilir  
- Örnek: Naive Bayes, LDA  

### 🔍 Discriminative (Logistic Regression, SVM)
- Sınıflar arasındaki sınırları öğrenir  
- **P(Y|X)** doğrudan öğrenilir  
- Örnek: Logistic Regression, SVM, Neural Networks  

---

## 🧂 Laplace Smoothing (0’dan Kaçış)

Bazı kelimeler eğitim verisinde hiç geçmeyebilir. Bu durumda:

- Olasılık = 0 olur  
- Tüm çarpım = 0 olur

Bu sorunu çözmek için **Laplace düzeltmesi (+1 smoothing)** yapılır:

$$
P(w|y) = \frac{\text{kelime sayısı} + 1}{\text{toplam kelime sayısı} + \text{kelime çeşit sayısı}}
$$

---

## 📉 Düşük Varyans Özelliği

Naive Bayes genellikle **kararlı (low variance)** bir modeldir.  
Farklı eğitim setleriyle sonuçları çok değişmez.  
Ancak bu durum esnekliği azaltır → **yüksek bias** problemi doğabilir.

---

## 🧪 Kullanım Alanları

- 📧 Spam e-posta tespiti  
- 😊 Duygu analizi  
- 📂 Doküman sınıflandırma  
- 🩺 Basit tıbbi teşhis sistemleri  

> 💡 **İpucu:** Özellik sayısı çok ama veri azsa, Naive Bayes iyi bir başlangıç modelidir.

---

## 🛠️ Notlar

- Naive Bayes hem **Multinomial**, hem **Gaussian**, hem de **Bernoulli** versiyonları ile çeşitli veri tiplerine uygulanabilir.
- Her ne kadar basit olsa da, baseline model olarak çoğu NLP probleminde hala güçlüdür.
