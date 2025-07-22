# 🧠 Support Vector Machines (SVM) — Derinlemesine Özet

Support Vector Machines (SVM), güçlü bir denetimli öğrenme algoritmasıdır. En çok **sınıflandırma** problemlerinde kullanılır, fakat **regresyon** için de uyarlanabilir (SVR).

---

## 🔍 SVM Ne Yapar?

SVM'in temel hedefi:
> **Veri noktalarını ayıran doğrusal bir karar sınırı (hiper düzlem) bulmak.**

Amaç:
- Eğitim verisini **iki sınıfa** ayıran **doğru(lar)** bulmak.
- Bu doğrular (veya hiper düzlemler) arasından, sınıfları ayıran en iyi olanı seçmek:  
  ➤ Bu da **sınıflara en yakın veri noktalarına olan mesafeyi (marjin) maksimize eden** doğrudur.

---

## 🧱 Temel Bileşenler

### ✅ **Support Vector Nedir?**

- Sınıflandırma sınırına en yakın olan **veri noktalarıdır.**
- Bu noktalar, karar sınırının tam yerini belirler.
- **Modelin yalnızca bu noktalara göre belirlenmesi**, SVM’in "sparse" (seyrek) doğasını oluşturur.

### ⚖️ **C Parametresi ve Trade-off**

- **C**, **marjin genişliği ile sınıflandırma hatası arasındaki dengeyi** kontrol eder.
- Küçük C → Daha büyük marjin ama bazı yanlış sınıflandırmalar kabul edilir.
- Büyük C → Hataları tolere etmez, ama marjin küçülür ve **overfitting riski artar.**

---

## 🚀 SVM’in Gücü Nereden Geliyor?

### 🎯 **Linearly Separable (Doğrusal Ayrılabilir) Veriler İçin:**
- SVM maksimum marjinli **hiper düzlem** bulur → Mükemmel çalışır.

### 🔄 **Linearly Non-Separable Veriler İçin:**
- Veriyi başka bir uzaya **projeksiyonla taşırız.**
- Bu yeni uzayda veri **doğrusal ayrılabilir hale gelir.**
- Bu sayede orada yine bir hiper düzlem bulunabilir.

---

## 📈 Cover's Theorem

> "High-dimensional spaces tend to make data more separable."

- Yani, **veri boyutu arttıkça doğrusal ayrılabilir hale gelme olasılığı artar.**
- Bu SVM’in projeksiyon stratejisine temel sağlar:  
  Veri orijinal uzayda ayrılamıyorsa, daha yüksek boyutlara taşı → Ayır!

---

## 🧠 Kernel Trick — SVM’in Gizli Gücü

SVM’in matematiksel yapısında, **veri noktalarının kendisine değil, sadece aralarındaki iç çarpımlara** (dot product) ihtiyaç vardır.

### 🧩 Problem:
- Veriyi yüksek (hatta sonsuz) boyutlara taşımak **hesaplama olarak pahalıdır.**

### ✨ Çözüm: Kernel Trick

> **Kernel fonksiyonu**, yüksek boyutlu uzayda yapılacak iç çarpımı, doğrudan orijinal uzaydaki iki nokta üzerinden hesaplar.

---

## 🔬 Kernel Nedir?

- İki veri noktasını alır, sanki yüksek boyutlu bir uzaya projekte edilmişler gibi **iç çarpım sonucunu** verir.
- Böylece yüksek boyutlara çıkmaya **gerek kalmaz**, ama etkisi alınır.

### 🎓 Teknik Tanım:

Bir kernel fonksiyonu \( K(x, y) \),  
yüksek boyutlu uzayda:  
\[
K(x, y) = \phi(x) \cdot \phi(y)
\]  
Ama biz doğrudan:
\[
K(x, y) = \text{some function of } x \text{ and } y
\]
olarak hesaplarız.

---

## 📊 Neden Kernel Kullanılır?

Örnek:

Projeksiyon yaparsak:
- Her nokta için 4 işlem → 2 nokta = 8 işlem
- Dot product = 3 işlem → toplam: **13 işlem**

Kernel ile:
- 2 çarpma + 1 toplama + kare alma = **4 işlem**

Bu fark, yüksek boyutlu veride **binlerce kat hız farkına** dönüşür.

---

## 🧪 Sık Kullanılan Kernel Fonksiyonları

### 1. **Linear Kernel**  
\[
K(x, y) = x \cdot y
\]  
Orijinal uzaydaki iç çarpım — hiçbir projeksiyon yok.

---

### 2. **Polynomial Kernel**  
\[
K(x, y) = (x \cdot y + c)^d
\]  
- \(c\): Bias terimi  
- \(d\): Polinom derecesi  
- Örnek: \(c = 0\), \(d = 2\) → ikinci dereceden projeksiyon

---

### 3. **RBF (Radial Basis Function / Gaussian Kernel)**  
\[
K(x, y) = \exp(-\gamma \|x - y\|^2)
\]  
- Sonsuz boyutlu projeksiyon etkisi verir  
- Uzak noktaları sıfıra yakınlaştırır, yakın noktaları 1’e yaklaştırır

---

### 4. **Sigmoid Kernel**  
\[
K(x, y) = \tanh(\alpha x \cdot y + c)
\]  
- Eski neural net aktivasyonlarına benzer  
- Çoğu durumda RBF’den daha az etkilidir.

---

## 🎯 Kernel Seçiminde Pratik Notlar

- Her kernel her veri seti için **iyi çalışmaz.**
- Başlangıçta:
  - Linear ve RBF kernel ile test yap
  - Sonra polynomial kernel ile varyasyonlar dene
- Grid Search + Cross Validation ile **en uygun kernel ve parametreler** bulunur.

---

## 🔚 Özet

| Bileşen | Açıklama |
|--------|----------|
| SVM'in görevi | Maksimum marjinli ayırıcı hiper düzlemi bulmak |
| Support Vector | Karar sınırına en yakın noktalar |
| C parametresi | Marjin ve hata arasındaki dengeyi ayarlar |
| Kernel | Projeksiyon yapmadan yüksek boyutlu iç çarpımı sağlar |
| RBF | Sonsuz boyut etkisi veren kernel |
| Cover's Theorem | Boyut arttıkça ayrılabilirlik artar |

---

> "With the right kernel, we don’t need to know how the data is projected — only what the inner product would have been."  

---  
**🧠 Kaynaklar:**  
- Vapnik, *Statistical Learning Theory*  
- scikit-learn SVM Documentation  
- CS229 - Stanford ML Lectures

