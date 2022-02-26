# Turkish-Wikipedi-Categorical-Web-Scraper

## With this repo, you can collect thousands of Turkish categorical data from Wikipedia. 

It can be very difficult to find labeled data in a certain category for the Turkish language. To solve this problem, categorically the best data is available on wikipedia.
With this repo, you can extract as much categorical clean data as you want from the field you want from wikipedia.

After the data is scraped, it is pre-processed and cleaned.

### Descriptions of the parameters of the two main functions

#### Func : categorical_scraper

```
    It is used to categorically pull data from Wikipedia.
 
    :param CATEGORY_QUERY: The category query to scrape.
    :type CATEGORY_QUERY: str

    :param save_path: The path where the extracted data will be saved.
    :type save_path: str

    :param LIMIT: Data limit to be extracted. If not given, it pulls all data.
    :type LIMIT: int

    :param page_per_save: It allows saving the categorical data extracted at the specified interval.
    :type page_per_save: int

    :param text_into_sentences_param: Specifies whether to save the extracted data in sentences or as text.
    :type text_into_sentences_param: bool

    :param remove_numbers: Determines whether to delete digits from the extracted data.
    :type remove_numbers: bool

    :param just_title_analysis: It only allows the header information of the pages to be collected.
    :type just_title_analysis: bool
 
```

#### Func : text_scraper_from_pagelist

```
    Wikipedia üzerinden kategorik olarak veri çekmek için kullanılır.
 
    :param page_list_path: Allows header information to be extracted from stored pages
    :type page_list_path: str
 
    :param save_path: The path where the extracted data will be saved.
    :type save_path: str
 
    :param page_per_save: It allows saving the categorical data extracted at the specified interval.
    :type page_per_save: int
 
    :param text_into_sentences_param: Specifies whether to save the extracted data in sentences or as text.
    :type text_into_sentences_param: bool
 
    :param remove_numbers: Determines whether to delete digits from the extracted data.
    :type remove_numbers: bool
 
    :param RANGE: Specifies the range of data to be extracted. It is used as "RANGE = [500,1000]". All data is extracted when not in use.
    :type RANGE: list
```

#### Example Usage:

```python
import WikiWebScraper

PATH = "_path_to_save_" 
scraper = WikiWebScraper() 

# It is used to categorically pull data from Wikipedia.
scraper.categorical_scraper("II._Dünya_Savaşı", PATH, 20, text_into_sentences_param=False)

# If you run the "categorical_scraper" function with the "just_title_analysis=True" parameter, 
# it only saves the titles of the categorical content to a file. This function is used to download 
# the content of the content titles in that file.
scraper.text_scraper_from_pagelist("page_list_path", "save_path" , page_per_save=1000) 

```

**Output:**
```
Sayfa taranıyor.: 100%|██████████| 20/20 [00:00<00:00, 92.01it/s]
Sayfa Ayrıştırılıyor: 100%|██████████| 20/20 [00:02<00:00,  7.71it/s]

20 adet sayfa bulundu ve içerisinden 20 satır farklı metin ayrıştırıldı.
```

**Example Data without "just_title_analysis=True" parameter(Category:Bilim, First 5 cleaned data)**
```
Felsefe-Bilim, Teoman Duralı ve İhsan Fazlıoğlu tarafından geliştirilen kuramdır.
Buna göre, felsefe-bilim 'genel felsefe' olarak adlandırılıan disiplinden başkalaşır.
Onun ucu bucağı görünmezliğine karşı tarihi-sistematik bir bölümüdür.
Felsefe-bilim şeklinde ortaya çıkan felsefe yapma tavrının kökleri Mısır ve Mezopotamya'ya uzanır.
Ancak onu hocası Eflatun'dan ilahi-uhrevi hikmet sancağını devralarak Aristoteles başlatmıştır.

```

**Example Data with "just_title_analysis=True" parameter(Category:II. Dünya Savaşı, First 10 title)**
```
/wiki/22._Panzer_T%C3%BCmeni_(Wehrmacht)
/wiki/38._Piyade_T%C3%BCmeni_(Wehrmacht)
/wiki/Agorelitsas_Sava%C5%9F%C4%B1
/wiki/Almanya%27n%C4%B1n_teslimiyet_belgesi
/wiki/Amfilochia_Sava%C5%9F%C4%B1
```
