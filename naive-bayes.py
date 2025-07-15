import streamlit as st

st.set_page_config(page_title="Naive Bayes Explained", layout="wide")

st.title("🔍 Naive Bayes Algoritması")

# Nedir?
st.header("📌 Naive Bayes Nedir?")
st.markdown("""
Naive Bayes, olasılıksal bir **sınıflandırma algoritmasıdır**.

🧠 **Genellikle:**  
- Metin sınıflandırma  
- Spam filtreleme  
- Duygu analizi gibi görevlerde kullanılır.

🔗 **Naive Varsayım:**  
Özelliklerin (örneğin kelimeler) birbirinden **bağımsız** olduğu varsayılır.
""")

st.divider()

# Temel Formüller
st.header("⚙️ Temel Formüller")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📐 Bayes Teoremi")
    st.latex(r"P(Y \mid x_1, \dots, x_n) = \frac{P(Y) \cdot \prod_{i=1}^n P(x_i \mid Y)}{P(x_1, \dots, x_n)}")
    st.caption("→ Gözlemlenen verilere göre Y sınıfının olasılığını verir.")

with col2:
    st.subheader("📐 Naive Bayes Formülü")
    st.latex(r"P(Y|x_1, ..., x_n) \propto P(Y) \prod_{i=1}^{n} P(x_i|Y)")
    st.caption("→ Özelliklerin birbirinden bağımsız olduğu varsayımıyla sadeleşir.")

st.divider()

# Ne Öğrenmez?
st.header("🚫 Model Ne Öğrenmez?")
st.warning("""
Naive Bayes **şunları öğrenmez**:
- Hangi özellikler daha belirleyicidir?
- Özellikler arasında etkileşim var mı?

Sadece **koşullu olasılıklara** bakar.
""")

# Avantajlar & Dezavantajlar
col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ Avantajlar")
    st.markdown("""
    - Hızlı ve basit  
    - Az veriyle bile etkili  
    - Yüksek boyutlu verilerle iyi çalışır  
    - Overfitting'e karşı dayanıklı  
    """)

with col2:
    st.subheader("❌ Dezavantajlar")
    st.markdown("""
    - Özellik bağımsızlığı varsayımı genelde geçersiz  
    - Özellik önemi öğrenilmez  
    - Sürekli veride dağılım **normal (Gaussian)** kabul edilir  
    """)

st.divider()

# Generative vs Discriminative
st.header("📚 Generative vs Discriminative")
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔁 Generative (Naive Bayes)")
    st.markdown("""
    - Her sınıf için verinin oluşumunu modellemeye çalışır  
    - **P(X|Y)** ve **P(Y)** öğrenilir  
    - Örnek: Naive Bayes, LDA  
    """)

with col2:
    st.subheader("🔍 Discriminative (Logistic Regression, SVM)")
    st.markdown("""
    - Sınıflar arasındaki sınırları öğrenir  
    - **P(Y|X)** doğrudan öğrenilir  
    - Örnek: Logistic Regression, SVM, Neural Networks  
    """)

st.divider()

# Laplace Smoothing
st.header("🧂 Laplace Smoothing (0’dan Kaçış)")
st.markdown("""
Eğitim verisinde bazı kelimeler hiç gözükmemiş olabilir.  
Bu, olasılığı sıfıra indirir ve tüm çarpımı bozar.

🧪 Bunu engellemek için **+1 smoothing (Laplace düzeltmesi)** yapılır:

\[
P(w|y) = \frac{\text{kelime sayısı} + 1}{\text{toplam kelime sayısı} + \text{kelime çeşit sayısı}}
\]
""")

# Düşük Varyans
st.header("📉 Düşük Varyans Özelliği")
st.info("""
Naive Bayes genellikle **kararlı (low variance)** bir modeldir.  
Farklı eğitim setleriyle sonuçları çok değişmez.  
Ancak bu durum bazen esnekliği düşürür (**yüksek bias**).
""")

# Kullanım Alanları
st.header("🧪 Kullanım Alanları")
st.markdown("""
📌 Naive Bayes şu alanlarda kullanılır:
- 📧 Spam e-posta tespiti  
- 😊 Duygu analizi  
- 📂 Doküman sınıflandırma  
- 🩺 Basit tıbbi teşhis sistemleri  
""")

st.success("✨ İpucu: Özellik sayısı çok ama veri azsa, Naive Bayes iyi bir başlangıç modelidir.")
