# Разведка (Reconnaissance)

## 1. Сбор информации о домене и IP

### WHOIS - Информация о домене
```bash
whois example.com
```

### nslookup - DNS запросы
```bash
nslookup example.com
nslookup -type=mx example.com    # MX записи
nslookup -type=txt example.com   # TXT записи
nslookup -type=ns example.com    # NS записи
```

### dig - DNS запросы (расширенный)
```bash
dig example.com
dig example.com MX
dig example.com TXT
dig example.com ANY              # Все записи
dig -x 8.8.8.8                   # Обратный DNS
```

### host - DNS lookup
```bash
host example.com
host -t mx example.com
host -a example.com
```

---

## 2. Поиск поддоменов (Subdomain Enumeration)

### Sublist3r
```bash
python3 sublist3r.py -d example.com -o subdomains.txt
python3 sublist3r.py -d example.com -v    # verbose режим
```

### Amass
```bash
amass enum -d example.com -o subdomains.txt
amass enum -passive -d example.com         # Пассивный режим
amass intel -d example.com                 # Разведка
amass enum -brute -d example.com           # Брутфорс поддоменов
```

### Subfinder
```bash
subfinder -d example.com -o subdomains.txt
subfinder -d example.com -all              # Все источники
subfinder -d example.com -silent           # Тихий режим
```

### Gobuster (DNS режим)
```bash
gobuster dns -d example.com -w wordlist.txt -o results.txt
```

### OneForAll
```bash
python3 oneforall.py --target example.com run
python3 oneforall.py --targets domains.txt run
```

---

## 3. Поисковые системы (OSINT)

### Google Dorks
```
site:example.com                    # Все страницы сайта
site:example.com inurl:admin        # Админ страницы
site:example.com filetype:pdf       # PDF файлы
site:example.com intitle:"index of" # Открытые директории
site:example.com ext:sql|env|bak    # Чувствительные файлы
```

### theHarvester - Сбор email и субдоменов
```bash
theHarvester -d example.com -b google,bing,linkedin
theHarvester -d example.com -b all -l 500
theHarvester -d example.com -b shodan
```

### Recon-ng - Модульная разведка
```bash
recon-ng
[recon-ng] marketplace install    # Установка всех модуелей
[recon-ng] modules load           # Загрузка модулей

# Пример использования:
[recon-ng] use recon/domains-hosts/google_site_web
[recon-ng] set SOURCE example.com
[recon-ng] run
```

---

## 4. Сканирование портов и сервисов

### Nmap - Основной инструмент
```bash
# Базовое сканирование
nmap example.com
nmap 192.168.1.0/24

# Сканирование всех портов
nmap -p- example.com
nmap -p 1-65535 example.com

# Определение версий сервисов
nmap -sV example.com

# Определение ОС
nmap -O example.com

# Агрессивное сканирование
nmap -A example.com

# Скрипты NSE
nmap --script=default example.com
nmap --script=vuln example.com
nmap --script=http-enum example.com
nmap --script=http-headers example.com
nmap --script=http-methods example.com
nmap --script=http-robots.txt example.com
nmap --script=http-sql-injection example.com
nmap --script=http-xssed example.com

# Полное сканирование
nmap -sS -sV -sC -O -p- -T4 example.com

# Скрытое сканирование (SYN)
nmap -sS example.com

# Сканирование UDP
nmap -sU --top-ports 100 example.com

# Вывод в файл
nmap -oN output.txt example.com
nmap -oX output.xml example.com
nmap -oA output example.com

# Сканирование из списка
nmap -iL targets.txt
```

### Masscan - Быстрое сканирование
```bash
masscan -p1-65535 example.com --rate=1000
masscan -p80,443,8080 192.168.1.0/24 --rate=10000
masscan -p0-65535 example.com -oG output.txt
```

### Rustscan - Современный сканер
```bash
rustscan -a example.com -- -sV -sC
rustscan -a example.com -p 1-65535
```

---

## 5. Технологии и стек (Technology Stack)

### WhatWeb - Определение технологий
```bash
whatweb example.com
whatweb example.com -v              # verbose
whatweb example.com -a 3            # Максимальная агрессия
whatweb example.com --log-json=output.json
```

### Wappalyzer (CLI)
```bash
wappalyzer https://example.com
wappalyzer https://example.com --pretty
```

### HTTPX - HTTP зондирование
```bash
httpx -u example.com
httpx -l subdomains.txt
httpx -l subdomains.txt -title -tech-detect -status-code
httpx -l targets.txt -o alive.txt
httpx -u example.com -json -o output.json
```

---

## 6. Скриншоты веб-сайтов

### Aquatone - Скриншоты поддоменов
```bash
cat subdomains.txt | aquatone
aquatone -out output_dir
```

### GoWitness - Скриншоты
```bash
gowitness single https://example.com
gowitness scan -c 10 -f subdomains.txt
gowitness file -f urls.txt
```

### http2png
```bash
http2png -u https://example.com -o screenshot.png
```

---

## 7. Поиск чувствительных файлов и директорий

### Gobuster - Брутфорс директорий
```bash
# Обычный брутфорс директорий
gobuster dir -u https://example.com -w wordlist.txt

# С расширениями
gobuster dir -u https://example.com -w wordlist.txt -x php,txt,html,bak,zip

# С авторизацией
gobuster dir -u https://example.com -w wordlist.txt -a "admin:password"

# С cookie
gobuster dir -u https://example.com -w wordlist.txt -c "session=abc123"

# С User-Agent
gobuster dir -u https://example.com -w wordlist.txt -U "Mozilla/5.0"

# Игнорирование статусов
gobuster dir -u https://example.com -w wordlist.txt -s 200,301,302,403

# С дополнительными заголовками
gobuster dir -u https://example.com -w wordlist.txt -H "X-Forwarded-For: 127.0.0.1"

# Вывод результатов
gobuster dir -u https://example.com -w wordlist.txt -o results.txt
```

### Dirb
```bash
dirb https://example.com
dirb https://example.com /usr/share/wordlists/dirb/common.txt
dirb https://example.com -X .php,.txt,.bak
dirb https://example.com -u
```

### Dirbuster
```bash
java -jar DirBuster.jar
```

### FFuf - Универсальный фаззер
```bash
# Брутфорс директорий
ffuf -u https://example.com/FUZZ -w wordlist.txt

# С расширениями
ffuf -u https://example.com/FUZZ -w wordlist.txt -e .php,.txt,.html

# С фильтрацией по статусу
ffuf -u https://example.com/FUZZ -w wordlist.txt -fc 404

# С фильтрацией по размеру
ffuf -u https://example.com/FUZZ -w wordlist.txt -fs 0

# Брутфорс параметров
ffuf -u https://example.com/search?q=FUZZ -w wordlist.txt

# Брутфорс заголовков
ffuf -u https://example.com -w wordlist.txt -H "Host: FUZZ"

# POST запросы с данными
ffuf -u https://example.com/login -X POST -d "user=admin&pass=FUZZ" -w passwords.txt

# Rate limiting
ffuf -u https://example.com/FUZZ -w wordlist.txt -rate 10

# Вывод результатов
ffuf -u https://example.com/FUZZ -w wordlist.txt -o results.json -of json
```

---

## 8. API и эндпоинты

### Arjun - Поиск параметров
```bash
arjun -u https://example.com/page
arjun -u https://example.com/page -m GET,POST
arjun -u https://example.com/page -w params.txt
```

### LinkFinder - Поиск ссылок в JS
```bash
python3 linkfinder.py -i https://example.com/script.js -o cli
python3 linkfinder.py -i https://example.com -o results.html
```

### JSParser - Парсинг JavaScript
```bash
python3 jsparser.py -u https://example.com -f jsfiles.txt
```

---

## 9. Автоматизация и фреймворки

### Reconftw - Автоматическая разведка
```bash
./reconftw.sh -d example.com -o output
./reconftw.sh -l domains.txt -o output
./reconftw.sh -d example.com --deep
```

### AutoRecon
```bash
autorecon example.com
autorecon -vv example.com          # verbose
autorecon -p 1-65535 example.com
```

### Sn1per
```bash
sniper -t example.com
sniper -t example.com -m full
sniper -t example.com -m port
```

---

## 10. Полезные Wordlist'ы

### Расположение в Kali Linux
```bash
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
/usr/share/wordlists/seclists/Discovery/DNS/
/usr/share/wordlists/seclists/Discovery/Web-Content/
```

### Seclists (установка)
```bash
apt install seclists
git clone https://github.com/danielmiessler/SecLists.git
```

### Популярные wordlist'ы
- **dirb/common.txt** - базовый для директорий
- **raft-large-directories.txt** - большие директории
- **directory-list-2.3-medium.txt** - средний список
- **subdomains-top1million-110000.txt** - поддомены

---

## 11. Специфические инструменты

### Shodan CLI - Поисковик устройств
```bash
shodan init API_KEY
shodan search "org:Company country:US"
shodan search "port:80 apache country:RU"
shodan host 1.2.3.4
shodan stats --facets org "apache"
```

### Censys CLI
```bash
censys search "example.com" hosts
censys view 1.2.3.4
censys stats
```

### Eyewitness - Скриншоты + отчёты
```bash
python3 EyeWitness.py --web -f urls.txt -d output
python3 EyeWitness.py --single -u https://example.com
```

---

## 12. Комбинации и пайплайны

### Полный пайплайн разведки
```bash
# 1. Сбор поддоменов
subfinder -d example.com -silent | httpx -silent -o alive.txt

# 2. Сканирование портов
nmap -sS -sV -p- -T4 --open -iL alive.txt -oA nmap_results

# 3. Брутфорс директорий
cat alive.txt | while read url; do
    gobuster dir -u "$url" -w wordlist.txt -x php,txt -t 50 -o "gobuster_$(echo $url | tr '/' '_').txt"
done

# 4. Скриншоты
gowitness scan -c 10 -f alive.txt

# 5. Технологии
cat alive.txt | while read url; do
    whatweb "$url" >> technologies.txt
done
```

---

## Шпаргалка по основным командам

| Задача | Команда |
|--------|---------|
| Информация о домене | `whois example.com` |
| DNS записи | `dig example.com ANY` |
| Поддомены | `subfinder -d example.com` |
| Сканирование портов | `nmap -sS -sV -p- example.com` |
| Директории | `gobuster dir -u URL -w wordlist.txt` |
| Скриншоты | `gowitness scan -f urls.txt` |
| Технологии | `whatweb URL` |
| Живые хосты | `httpx -l subdomains.txt` |
| OSINT | `theHarvester -d example.com -b all` |
