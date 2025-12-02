## Tren Rezervasyon API
Bu proje, FastAPI kullanılarak geliştirilmiş basit bir tren rezervasyon servisidir.
Yolcuların vagonlara yerleştirilip yerleştirilemeyeceğini hesaplar ve uygun yerleşim planını JSON olarak döner.

## Kurulum
pip install -r requirements.txt
uvicorn main:app --reload

## Kullanım
Swagger UI: http://127.0.0.1:8000/docs


## Örnek İstek
{
  "Tren": {
    "Ad": "Başkent Ekspres",
    "Vagonlar": [
      { "Ad": "Vagon 1", "Kapasite": 100, "DoluKoltukAdet": 68 },
      { "Ad": "Vagon 2", "Kapasite": 90, "DoluKoltukAdet": 50 },
      { "Ad": "Vagon 3", "Kapasite": 80, "DoluKoltukAdet": 80 }
    ]
  },
  "RezervasyonYapilacakKisiSayisi": 3,
  "KisilerFarkliVagonlaraYerlestirilebilir": true
}

## Örnek Yanıt
{
  "RezervasyonYapilabilir": true,
  "YerlesimAyrinti": [
    { "VagonAdi": "Vagon 1", "KisiSayisi": 2 },
    { "VagonAdi": "Vagon 2", "KisiSayisi": 1 }
  ]
}

## Dosya Yapısı
<pre>```plaintexttren-rezervasyon-api/├── main.py├── requirements.txt└── README.md```</pre>