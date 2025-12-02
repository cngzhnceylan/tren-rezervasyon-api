from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Vagon(BaseModel):
    Ad: str
    Kapasite: int
    DoluKoltukAdet: int

class Tren(BaseModel):
    Ad: str
    Vagonlar : List[Vagon]

class RezervasyonRequest(BaseModel):
    Tren : Tren
    RezervasyonYapilacakKisiSayisi: int
    KisilerFarkliVagonlaraYerlestirilebilir: bool

@app.post("/rezervasyon")
def rezervasyon_yap(request: RezervasyonRequest):
    """
    Tren rezervasyonu yapar.
    Yolculari vagonlara %70 kapasite kuralina göre yerleştirir.
    """
    yerlesimAyrinti = []
    # Rezervasyon yapılacak kişi sayısını al
    kalanKisiSayisi = request.RezervasyonYapilacakKisiSayisi
    # Her vagon için uygun koltuk sayısını kontrol et
    for vagon in request.Tren.Vagonlar:
        # Vagon başına %70 doluluk oranı ile rezervasyon yapılabilir
        uygunKoltukSayisi = int((vagon.Kapasite * 0.7) - vagon.DoluKoltukAdet)
        if uygunKoltukSayisi <= 0:
            continue
        else:
            if kalanKisiSayisi > 0:
                # Kişiler farklı vagonlara yerleştirilebilir ise
                if request.KisilerFarkliVagonlaraYerlestirilebilir:
                    yerlestirilenYolcuSayisi = min(uygunKoltukSayisi, kalanKisiSayisi)
                    yerlesimAyrinti.append({"VagonAdi": vagon.Ad,"KisiSayisi": yerlestirilenYolcuSayisi})
                    #yerleştirilen yolcu sayısını kalan kişiden düş
                    kalanKisiSayisi -= yerlestirilenYolcuSayisi
                # Kişiler farklı vagonlara yerleştirilemez ise
                else:
                    if uygunKoltukSayisi >= request.RezervasyonYapilacakKisiSayisi:
                        yerlesimAyrinti.append({"VagonAdi": vagon.Ad,"KisiSayisi": request.RezervasyonYapilacakKisiSayisi})
                        #tek vagonda tüm kişileri yerleştirildiği için kalanKisiSayisi=0
                        kalanKisiSayisi = 0
                        break
    # Burada kalanKisiSayisi 0 ise rezervasyon yapılabilir
    if kalanKisiSayisi == 0:
        return {
            "RezervasyonYapilabilir": True,
            "YerlesimAyrinti": yerlesimAyrinti,
        }
    else:
        return {
            "RezervasyonYapilabilir": False,
            "YerlesimAyrinti": [],
        }



