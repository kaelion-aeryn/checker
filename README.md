# Flashback VPN Advanced Proxy Checker

Checker proxy canggih yang bisa test HTTP, SOCKS4, dan SOCKS5 dengan menu pilihan interaktif.

## 🚀 Fitur Utama

- ✅ **HTTP Proxy Checker** - Test proxy HTTP
- ✅ **SOCKS4 Proxy Checker** - Test proxy SOCKS4  
- ✅ **SOCKS5 Proxy Checker** - Test proxy SOCKS5
- ✅ **Test All Types** - Test semua tipe sekaligus
- ✅ **Multi-threading** - 10 thread concurrent untuk kecepatan
- ✅ **Auto-save** - Proxy yang work otomatis disimpan
- ✅ **Menu Interaktif** - Pilihan mudah dengan menu
- ✅ **Error Handling** - Penanganan error yang robust
- ✅ **Timeout Protection** - 10 detik timeout per proxy

## 📋 Cara Penggunaan

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Siapkan File Proxy
Pastikan file `proxy.txt` berisi daftar proxy dalam format:
```
IP:PORT
192.168.1.1:1080
10.0.0.1:8080
```

### 3. Jalankan Advanced Checker
```bash
python checker_advanced.py
```

## 🎯 Menu Pilihan

```
🔍 Flashback VPN Advanced Proxy Checker
==================================================
1. HTTP Proxy Checker
2. SOCKS4 Proxy Checker
3. SOCKS5 Proxy Checker
4. Test All Types (HTTP + SOCKS4 + SOCKS5)
5. Keluar
==================================================
```

## 📊 Output Format

### HTTP Proxy
- **Work**: `✅ HTTP Proxy Bisa Dituyul (Telah Disimpan Ke work.txt)`
- **Error**: `❌ Error Buang HTTP Proxy (Connection Error)`

### SOCKS4 Proxy  
- **Work**: `✅ SOCKS4 Proxy Bisa Dituyul (Telah Disimpan Ke work.txt)`
- **Error**: `❌ Error Buang SOCKS4 Proxy (Timeout)`

### SOCKS5 Proxy
- **Work**: `✅ SOCKS5 Proxy Bisa Dituyul (Telah Disimpan Ke work.txt)`
- **Error**: `❌ Error Buang SOCKS5 Proxy (Connection Error)`

### Test All Types
- **Work**: `HTTP: ✅ HTTP Proxy Bisa Dituyul | SOCKS4: ✅ SOCKS4 Proxy Bisa Dituyul`
- **Error**: `❌ Error Buang Proxy (Semua tipe gagal)`

## 📁 File Output

### work.txt Format
```
# Untuk single type test
192.168.1.1:1080 (HTTP)
10.0.0.1:8080 (SOCKS4)
172.16.0.1:1080 (SOCKS5)

# Untuk test all types
192.168.1.1:1080 (WORKING)
10.0.0.1:8080 (WORKING)
```

## 🎯 Target Testing

Checker akan test proxy terhadap:
`https://distribute.flashbacktochina.com/index.php?s=/wap/login/register`

## ⚙️ Konfigurasi

- **Timeout**: 10 detik per proxy
- **Max Workers**: 10 thread concurrent
- **Target URL**: Flashback VPN registration page
- **User-Agent**: Chrome browser spoofing

## 🔄 Perbedaan dengan Checker Basic

| Fitur | Basic Checker | Advanced Checker |
|-------|---------------|------------------|
| Proxy Types | SOCKS5 only | HTTP, SOCKS4, SOCKS5 |
| Menu System | ❌ | ✅ |
| Test All Types | ❌ | ✅ |
| Proxy Type Label | ❌ | ✅ |
| Interactive | ❌ | ✅ |
| Continue Option | ❌ | ✅ |

## 💡 Tips Penggunaan

1. **Untuk proxy HTTP**: Pilih opsi 1
2. **Untuk proxy SOCKS4**: Pilih opsi 2  
3. **Untuk proxy SOCKS5**: Pilih opsi 3
4. **Untuk test semua tipe**: Pilih opsi 4 (lebih lambat tapi lengkap)
5. **Untuk keluar**: Pilih opsi 5 atau tekan Ctrl+C

## 🚨 Catatan Penting

- File `work.txt` akan di-reset setiap kali menjalankan checker
- Proxy yang work akan disimpan dengan label tipe proxy
- Test "All Types" akan lebih lambat karena test 3x per proxy
- Gunakan Ctrl+C untuk menghentikan proses kapan saja 
