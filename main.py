import requests
import socks
import socket
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import sys

# Target URL untuk testing
TARGET_URL = "https://distribute.flashbacktochina.com/index.php?s=/wap/login/register"

# File untuk menyimpan proxy yang work (dipisah berdasarkan tipe)
HTTP_FILE = "http.txt"
SOCKS4_FILE = "socks4.txt"
SOCKS5_FILE = "socks5.txt"

def test_http_proxy(proxy):
    """
    Test proxy HTTP terhadap target URL
    """
    try:
        # Parse proxy string
        if ':' in proxy:
            host, port = proxy.strip().split(':')
            port = int(port)
        else:
            return False, f"Format proxy salah: {proxy}"
        
        # Setup HTTP proxy
        proxies = {
            'http': f'http://{host}:{port}',
            'https': f'http://{host}:{port}'
        }
        
        # Test request dengan timeout
        response = requests.get(
            TARGET_URL, 
            proxies=proxies,
            timeout=10,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        
        if response.status_code == 200:
            return True, f"✅ HTTP Proxy Bisa Dituyul (Telah Disimpan Ke {HTTP_FILE})"
        else:
            return False, f"❌ Error Buang HTTP Proxy (Status: {response.status_code})"
            
    except requests.exceptions.Timeout:
        return False, "❌ Error Buang HTTP Proxy (Timeout)"
    except requests.exceptions.ConnectionError:
        return False, "❌ Error Buang HTTP Proxy (Connection Error)"
    except Exception as e:
        return False, f"❌ Error Buang HTTP Proxy ({str(e)})"

def test_socks4_proxy(proxy):
    """
    Test proxy SOCKS4 terhadap target URL
    """
    # Simpan socket asli
    original_socket = socket.socket
    
    try:
        # Parse proxy string
        if ':' in proxy:
            host, port = proxy.strip().split(':')
            port = int(port)
        else:
            return False, f"Format proxy salah: {proxy}"
        
        # Setup SOCKS4 proxy
        socks.set_default_proxy(socks.SOCKS4, host, port)
        socket.socket = socks.socksocket
        
        # Test request dengan timeout
        response = requests.get(
            TARGET_URL, 
            timeout=10,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        
        if response.status_code == 200:
            return True, f"✅ SOCKS4 Proxy Bisa Dituyul (Telah Disimpan Ke {SOCKS4_FILE})"
        else:
            return False, f"❌ Error Buang SOCKS4 Proxy (Status: {response.status_code})"
            
    except requests.exceptions.Timeout:
        return False, "❌ Error Buang SOCKS4 Proxy (Timeout)"
    except requests.exceptions.ConnectionError:
        return False, "❌ Error Buang SOCKS4 Proxy (Connection Error)"
    except Exception as e:
        return False, f"❌ Error Buang SOCKS4 Proxy ({str(e)})"
    finally:
        # Selalu restore socket asli
        socket.socket = original_socket

def test_socks5_proxy(proxy):
    """
    Test proxy SOCKS5 terhadap target URL
    """
    # Simpan socket asli
    original_socket = socket.socket
    
    try:
        # Parse proxy string
        if ':' in proxy:
            host, port = proxy.strip().split(':')
            port = int(port)
        else:
            return False, f"Format proxy salah: {proxy}"
        
        # Setup SOCKS5 proxy
        socks.set_default_proxy(socks.SOCKS5, host, port)
        socket.socket = socks.socksocket
        
        # Test request dengan timeout
        response = requests.get(
            TARGET_URL, 
            timeout=10,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        
        if response.status_code == 200:
            return True, f"✅ SOCKS5 Proxy Bisa Dituyul (Telah Disimpan Ke {SOCKS5_FILE})"
        else:
            return False, f"❌ Error Buang SOCKS5 Proxy (Status: {response.status_code})"
            
    except requests.exceptions.Timeout:
        return False, "❌ Error Buang SOCKS5 Proxy (Timeout)"
    except requests.exceptions.ConnectionError:
        return False, "❌ Error Buang SOCKS5 Proxy (Connection Error)"
    except Exception as e:
        return False, f"❌ Error Buang SOCKS5 Proxy ({str(e)})"
    finally:
        # Selalu restore socket asli
        socket.socket = original_socket

def test_all_proxy_types(proxy):
    """
    Test proxy dengan semua tipe (HTTP, SOCKS4, SOCKS5)
    """
    results = []
    working_types = []
    
    # Test HTTP
    http_result, http_msg = test_http_proxy(proxy)
    if http_result:
        results.append(f"HTTP: {http_msg}")
        working_types.append("HTTP")
    
    # Test SOCKS4
    socks4_result, socks4_msg = test_socks4_proxy(proxy)
    if socks4_result:
        results.append(f"SOCKS4: {socks4_msg}")
        working_types.append("SOCKS4")
    
    # Test SOCKS5
    socks5_result, socks5_msg = test_socks5_proxy(proxy)
    if socks5_result:
        results.append(f"SOCKS5: {socks5_msg}")
        working_types.append("SOCKS5")
    
    if results:
        return True, " | ".join(results), working_types
    else:
        return False, "❌ Error Buang Proxy (Semua tipe gagal)", []

def save_working_proxy(proxy, proxy_type=""):
    """
    Simpan proxy yang work ke file berdasarkan tipe
    """
    try:
        if proxy_type == "HTTP":
            with open(HTTP_FILE, 'a', encoding='utf-8') as f:
                f.write(proxy + '\n')
        elif proxy_type == "SOCKS4":
            with open(SOCKS4_FILE, 'a', encoding='utf-8') as f:
                f.write(proxy + '\n')
        elif proxy_type == "SOCKS5":
            with open(SOCKS5_FILE, 'a', encoding='utf-8') as f:
                f.write(proxy + '\n')
        elif proxy_type == "ALL":
            # Untuk test all, simpan ke semua file yang work
            pass  # Akan dihandle di fungsi test_all_proxy_types
    except Exception as e:
        print(f"Error menyimpan proxy: {e}")

def save_working_proxy_all_types(proxy, working_types):
    """
    Simpan proxy yang work ke semua file yang sesuai
    """
    try:
        for proxy_type in working_types:
            if proxy_type == "HTTP":
                with open(HTTP_FILE, 'a', encoding='utf-8') as f:
                    f.write(proxy + '\n')
            elif proxy_type == "SOCKS4":
                with open(SOCKS4_FILE, 'a', encoding='utf-8') as f:
                    f.write(proxy + '\n')
            elif proxy_type == "SOCKS5":
                with open(SOCKS5_FILE, 'a', encoding='utf-8') as f:
                    f.write(proxy + '\n')
    except Exception as e:
        print(f"Error menyimpan proxy: {e}")

def clear_output_files():
    """
    Bersihkan semua file output
    """
    files_to_clear = [HTTP_FILE, SOCKS4_FILE, SOCKS5_FILE]
    for file in files_to_clear:
        if os.path.exists(file):
            os.remove(file)

def show_menu():
    """
    Tampilkan menu pilihan
    """
    print("\n🔍 Flashback VPN Advanced Proxy Checker")
    print("=" * 50)
    print("1. HTTP Proxy Checker")
    print("2. SOCKS4 Proxy Checker") 
    print("3. SOCKS5 Proxy Checker")
    print("4. Test All Types (HTTP + SOCKS4 + SOCKS5)")
    print("5. Keluar")
    print("=" * 50)

def main():
    while True:
        show_menu()
        
        try:
            choice = input("Pilih opsi (1-5): ").strip()
            
            if choice == "5":
                print("👋 Terima kasih telah menggunakan checker!")
                break
            elif choice not in ["1", "2", "3", "4"]:
                print("❌ Pilihan tidak valid! Silakan pilih 1-5.")
                continue
            
            # Baca file proxy
            if not os.path.exists('proxy.txt'):
                print("❌ File proxy.txt tidak ditemukan!")
                continue
            
            with open('proxy.txt', 'r', encoding='utf-8') as f:
                proxies = [line.strip() for line in f if line.strip()]
            
            if not proxies:
                print("❌ Tidak ada proxy di file proxy.txt!")
                continue
            
            print(f"\n📋 Total proxy yang akan ditest: {len(proxies)}")
            print(f"🎯 Target URL: {TARGET_URL}")
            
            # Bersihkan file output
            clear_output_files()
            
            working_count = 0
            total_count = len(proxies)
            
            # Pilih fungsi test berdasarkan pilihan
            if choice == "1":
                test_func = test_http_proxy
                proxy_type = "HTTP"
                print("🌐 Testing HTTP proxies...")
            elif choice == "2":
                test_func = test_socks4_proxy
                proxy_type = "SOCKS4"
                print("🧦 Testing SOCKS4 proxies...")
            elif choice == "3":
                test_func = test_socks5_proxy
                proxy_type = "SOCKS5"
                print("🧦 Testing SOCKS5 proxies...")
            elif choice == "4":
                test_func = test_all_proxy_types
                proxy_type = "ALL"
                print("🔄 Testing all proxy types...")
            
            print("=" * 50)
            
            # Test proxy dengan threading
            with ThreadPoolExecutor(max_workers=10) as executor:
                # Submit semua proxy untuk testing
                future_to_proxy = {executor.submit(test_func, proxy): proxy for proxy in proxies}
                
                # Process results
                for future in as_completed(future_to_proxy):
                    proxy = future_to_proxy[future]
                    try:
                        if choice == "4":
                            is_working, message, working_types = future.result()
                        else:
                            is_working, message = future.result()
                        
                        print(f"{proxy}: {message}")
                        
                        if is_working:
                            if choice == "4":
                                # Untuk test all, simpan ke semua file yang work
                                save_working_proxy_all_types(proxy, working_types)
                                working_count += 1
                            else:
                                save_working_proxy(proxy, proxy_type)
                                working_count += 1
                            
                    except Exception as e:
                        print(f"{proxy}: ❌ Error Buang Proxy ({str(e)})")
            
            print("=" * 50)
            print(f"✅ Selesai! {working_count}/{total_count} proxy berhasil")
            
            # Tampilkan file yang dibuat
            if choice == "1":
                print(f"💾 HTTP proxy yang work disimpan di: {HTTP_FILE}")
            elif choice == "2":
                print(f"💾 SOCKS4 proxy yang work disimpan di: {SOCKS4_FILE}")
            elif choice == "3":
                print(f"💾 SOCKS5 proxy yang work disimpan di: {SOCKS5_FILE}")
            elif choice == "4":
                print(f"💾 Proxy yang work disimpan di:")
                if os.path.exists(HTTP_FILE):
                    print(f"   - {HTTP_FILE}")
                if os.path.exists(SOCKS4_FILE):
                    print(f"   - {SOCKS4_FILE}")
                if os.path.exists(SOCKS5_FILE):
                    print(f"   - {SOCKS5_FILE}")
            
            # Tanya apakah ingin lanjut
            continue_choice = input("\nApakah ingin test lagi? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("👋 Terima kasih telah menggunakan checker!")
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan oleh user!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 
