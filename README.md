#🌸 Iris Veri Seti Sınıflandırma Analizi

Bu proje, makine öğrenmesine girişin "Merhaba Dünya"sı kabul edilen Iris Veri Seti üzerinde, teorik olarak öğrendiğim sınıflandırma (classification) algoritmalarının pratik performanslarını karşılaştırmak amacıyla geliştirdiğim bir çalışmadır.


##📂 Veri Seti Hakkında (Dataset)
Analizimde kullandığım veri seti 150 satır ve 5 sütundan oluşmaktadır.
**Girdi Özellikleri (Features):**
-> sepal length: Çanak yaprak uzunluğu
-> sepal width: Çanak yaprak genişliği
-> petal length: Taç yaprak uzunluğu
-> petal width: Taç yaprak genişliği
**Hedef Sınıflar (Target):**
-> Iris-setosa
-> Iris-versicolor
-> Iris-virginica
Not: Veri setinde her sınıftan eşit sayıda (50'şer adet) örnek bulunmaktadır, yani dengeli (balanced) bir veri setidir.

###⚙️ Ön İşleme (Preprocessing)
Modelleri eğitmeden önce veriyi daha anlamlı hale getirmek için şu adımları uyguladım:
**Veri Bölme:** Veriyi %67 Eğitim, %33 Test olacak şekilde ayırdım (test_size=0.33).
**Ölçeklendirme (Scaling):** Algoritmaların (özellikle KNN ve SVM) mesafeye dayalı hesaplamalarında hata yapmaması için StandardScaler kullanarak verileri standartlaştırdım.

##🧠 Kullandığım Algoritmalar ve Analizler

###1. Logistic Regression (Lojistik Regresyon)
**Sonuç (Hata Sayısı):** 0 Hata
**Confusion Matrix:**
[[19  0  0]
 [ 0 15  0]
 [ 0  0 16]]
**Analiz: **Iris veri setinde sınıflar doğrusal olarak  çok net ayrılabiliyor. Lojistik Regresyon, verideki bu doğrusal sınırları mükemmel yakaladı ve %100 başarı sağladı. En verimli çalışan modelim bu oldu.

###2. K-Nearest Neighbors (KNN)
**Parametre:** n_neighbors=1, metric='minkowski'
**Sonuç (Hata Sayısı):** 3 Hata
**Confusion Matrix:**
[[19  0  0]
 [ 0 14  1]
 [ 0  2 14]]
**Analiz: **En yakın tek komşuya (k=1) bakarak karar vermek, modeli"gürültüye" karşı hassas hale getirdi. Sınıf sınırlarında kalan 3 adet veriyi, sadece en yakınındaki tek bir yanlış komşuya bakarak hatalı sınıflandırdı. k değerini 3 veya 5 seçmek çok daha iyi sonuç verecektir.

###3. Support Vector Machine (SVM)
**Parametre:** kernel='linear'
**Sonuç (Hata Sayısı):** 1 Hata
**Confusion Matrix:**
[[19  0  0]
 [ 0 14  1]
 [ 0  0 16]]
**Analiz**: SVM, sınıflar arasında en geniş güvenli yolu  çizmeye çalışır. Linear kernel kullanmama rağmen, veri uzayında sadece 1 noktada yanıldı. Oldukça kararlı  bir model.

###4. Naive Bayes (Gaussian)
**Sonuç (Hata Sayısı):** 2 Hata
**Confusion Matrix:**
[[19  0  0]
 [ 0 14  1]
 [ 0  1 15]]
**Analiz**: Bu algoritma, "tüm özellikler birbirinden bağımsızdır" (örneğin yaprak genişliği ile uzunluğu alakasızdır) gibi saf bir varsayımla çalışır. Biyolojik verilerde bu varsayım her zaman tutmasa da, algoritma şaşırtıcı derecede hızlı ve başarılı çalışarak sadece 2 hata yaptı.

###5. Decision Tree (Karar Ağacı)
**Parametre:** criterion='entropy'
**Sonuç (Hata Sayısı):** 2 Hata
**Confusion Matrix:**
[[19  0  0]
 [ 0 14  1]
 [ 0  1 15]]
**Analiz**: Veriyi "yaprak uzunluğu < 2.4 ise Setosa'dır" gibi kurallara bölerek ağaç oluşturdu. Küçük veri setlerinde aşırı öğrenme (overfitting) riski olsa da, entropy bu durum için iyi bir seçim oldu.

###6. Random Forest (Rastgele Orman)
**Parametre:** n_estimators=10, criterion='entropy'
**Sonuç (Hata Sayısı):** 1 Hata
**Confusion Matrix:**
[[19  0  0]
 [ 0 15  0]
 [ 0  1 15]]
**Analiz**: Tek bir karar ağacı 2 hata yaparken, 10 ağaçtan oluşan bu orman modeli hatayı 1'e düşürdü. "Topluluk Öğrenmesi" sayesinde, tek bir ağacın yaptığı hatayı çoğul ağaçalar kullanrak daha kararlı hale getirdim.

**Sonuç olarak;** hiçbir algoritma evrensel olarak 'kusursuz' veya 'hatalı' değildir. Önemli olan, eldeki verinin doğasını anlayarak ona en uygun algoritmayı seçmek ve parametreleri bu doğrultuda optimize etmektir.

##🚀 Kurulum ve Çalıştırma
**Projeyi kendi bilgisayarınızda çalıştırmak için:**
**Gerekli kütüphaneleri yükleyin:**
** -> pip install numpy pandas scikit-learn xlrd openpyxl**
** -> Repoyu klonlayın ve kodu çalıştırın.**


