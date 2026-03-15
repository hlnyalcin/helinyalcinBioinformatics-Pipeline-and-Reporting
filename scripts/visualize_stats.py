import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv("read_stats.csv")

# Özet istatistikleri yazdır
print(df.describe())

# Plotları oluştur
plt.figure(figsize=(15,5))

# GC Content
plt.subplot(1,3,1)
plt.hist(df['GC_Content'], bins=50, color='skyblue')
plt.title('GC Content Distribution')
plt.xlabel('GC %')
plt.ylabel('Number of Reads')

# Read Length
plt.subplot(1,3,2)
plt.hist(df['Read_Length'], bins=50, color='lightgreen')
plt.title('Read Length Distribution')
plt.xlabel('Length (bp)')

# Mean Quality
plt.subplot(1,3,3)
plt.hist(df['Mean_Quality'], bins=50, color='salmon')
plt.title('Mean Quality Score Distribution')
plt.xlabel('Mean Quality')

plt.tight_layout()
plt.show()
plt.savefig("read_stats_histograms.png")  # Grafikleri kaydeder
plt.show()  # Grafikleri ekranda gösterir
