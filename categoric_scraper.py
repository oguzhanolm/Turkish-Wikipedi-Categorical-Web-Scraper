def categorical_scraper(query, save_path, limit=-1, page_per_save=10000, text_into_sentences_param=True,
                        remove_numbers=False, just_title_analysis=False):
    """
    Wikipedia üzerinden kategorik olarak veri çekmek için kullanılır.

    :param query: Ayıklanacak kategori sorgusu.
    :type query: str

    :param save_path: Ayıklanan verinin kaydedileceği yol.
    :type save_path: str

    :param limit: Ayıklanması istenen veri limiti. Verilmediği taktirde tüm verileri çeker.
    :type limit: int

    :param page_per_save: Belirlenen aralıkla ayıklanan kategorik verinin kaydedilmesini sağlar.
    :type page_per_save: int

    :param text_into_sentences_param: Ayıklanan verilerin cümleler halinde mi, yoksa metin halinde mi kaydedileceğini belirler.
    :type text_into_sentences_param: bool

    :param remove_numbers: Ayıklanan verilerden rakamların silinip silinmemesini belirler.
    :type remove_numbers: bool

    :param just_title_analysis: Sadece sayfaların başlık bilgilerinin toplanmasını sağlar.
    :type just_title_analysis: bool
    """
    if limit == -1:
        limit = 99999999

    query = query.replace(" ", "_")
    HEADERS_PARAM = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

    from Scraper.scraping_tools import category_scraping_interface
    return_list = category_scraping_interface(query, limit, HEADERS_PARAM, save_path, page_per_save, remove_numbers,
                                              just_title_analysis, text_into_sentences_param)

    if return_list is None:
        return []
    else:
        return return_list

def text_scraper_from_pagelist(page_list_path, save_path, page_per_save=10000, remove_numbers=False,
                               text_into_sentences_param=True, RANGE=None):
    """

    Wikipedia üzerinden kategorik olarak veri çekmek için kullanılır.

    :param page_list_path: Toplanan sayfaların başlık bilgilerinin çıkartılmasını sağlar
    :type page_list_path: str

    :param save_path: Ayıklanan verinin kaydedileceği yol.
    :type save_path: str

    :param page_per_save: Belirlenen aralıkla ayıklanan kategorik verinin kaydedilmesini sağlar.
    :type page_per_save: int

    :param text_into_sentences_param: Ayıklanan verilerin cümleler halinde mi, yoksa metin halinde mi kaydedileceğini belirler.
    :type text_into_sentences_param: bool

    :param remove_numbers: Ayıklanan verilerden rakamların silinip silinmemesini belirler.
    :type remove_numbers: bool

    :param RANGE: Ayıklnacak verilerin aralığını belirler. "RANGE = [500,1000]" şeklinde kullanılır. Verilmediği zaman tüm veri ayıklanır.
    :type RANGE: list
    """

    text_list = []

    HEADERS_PARAM = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

    with open(page_list_path, 'r') as f:
        page_list = [line.strip() for line in f]

    if RANGE is not None:
        page_list = page_list[RANGE[0]:RANGE[1]]

    temp_range = 0
    loop_counter = 0

    from Scraper.scraping_tools import text_into_sentences,text_scraper,save_to_csv

    for i in range(page_per_save, len(page_list) + page_per_save, page_per_save):

        if loop_counter == (len(page_list) // page_per_save):
            PATH = save_path + "/" + "scraped_page" + "_" + str(temp_range) + " - " + str(len(page_list)) + ".txt"
            temp_text_list = text_into_sentences(
                text_scraper(page_list[temp_range:i], (len(page_list) % page_per_save), HEADERS_PARAM, True),
                remove_numbers, text_into_sentences_param)
        else:
            PATH = save_path + "/" + "scraped_page" + "_" + str(temp_range) + " - " + str(i) + ".txt"
            temp_text_list = text_into_sentences(
                text_scraper(page_list[temp_range:i], page_per_save, HEADERS_PARAM, True), remove_numbers,
                text_into_sentences_param)

        text_list += temp_text_list

        save_to_csv(PATH, temp_text_list)
        temp_range = i
        loop_counter += 1

    print("\n\"" + page_list_path + "\" konumundaki " + str(len(page_list)) + " adet sayfa içerisinden " + str(
        len(text_list)) + " satır metin ayrıştırıldı.")

    return text_list