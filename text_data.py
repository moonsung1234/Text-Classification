
from bs4 import BeautifulSoup as Bsoup
import requests as req
import csv
import re

url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=163834&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="
url2 = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=134963&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="

with open("sentences.csv", "w", newline="") as fp :
    wr = csv.writer(fp)

    texts = []
    scores = []
    count = 1

    for i in range(1, 301) :
        res = req.get(url + str(i))

        if res.status_code == 200 :
            soup = Bsoup(res.text, "html.parser")
            span_texts = soup.find_all(attrs={ "id" : re.compile("_filtered_ment_[0-9]") })
            div_scores = soup.find_all(attrs={ "class" : "star_score" })

            for span_text in span_texts :
                final_text = span_text.text.strip()
                texts.append(final_text)

            for div_score in div_scores :
                final_score = div_score.text.strip()
                scores.append(final_score)

        else :
            print("요청에 실패하였습니다. (Connection failed.)")

    for i in range(1, 1001) :
        res = req.get(url2 + str(i))

        if res.status_code == 200 :
            soup = Bsoup(res.text, "html.parser")
            span_texts = soup.find_all(attrs={ "id" : re.compile("_filtered_ment_[0-9]") })
            div_scores = soup.find_all(attrs={ "class" : "star_score" })

            for span_text in span_texts :
                final_text = span_text.text.strip()
                texts.append(final_text)

            for div_score in div_scores :
                final_score = div_score.text.strip()
                scores.append(final_score)

        else :
            print("요청에 실패하였습니다. (Connection failed.)")

    for li in list(zip(texts, scores)) :
        wr.writerow([count, li[0], li[1]])
        count += 1