import speedtest

def internet_hizi_testi():
    st = speedtest.Speedtest()
    
    print("En iyi sunucu bulunuyor...")
    st.get_best_server()  # En uygun sunucuyu seç
    
    print("İndirme hızı ölçülüyor...")
    download_speed = st.download() / 10**6  # Mbps cinsinden
    print(f"İndirme Hızı: {download_speed:.2f} Mbps")
    
    print("Yükleme hızı ölçülüyor...")
    upload_speed = st.upload() / 10**6  # Mbps cinsinden
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
    
    ping = st.results.ping  # Ping değeri (ms)
    print(f"Ping: {ping:.2f} ms")

internet_hizi_testi()
