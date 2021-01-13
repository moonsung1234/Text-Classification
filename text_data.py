
from bs4 import BeautifulSoup as Bsoup
import requests as req
import csv
import re

url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=163834&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="
url2 = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=134963&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="
url3 = "https://movie.naver.com/movie/point/af/list.nhn?&page="

with open("sentences.csv", "a", encoding="utf-8", newline="") as fp :
    wr = csv.writer(fp)

    count = 13501

    for i in range(1, 351) :
        res = req.get(url + str(i))

        if res.status_code == 200 :
            soup = Bsoup(res.text, "html.parser")
            span_texts = soup.find_all(attrs={ "id" : re.compile("_filtered_ment_[0-9]") })
            div_scores = soup.find_all(attrs={ "class" : "star_score" })

            text_score_list = list(zip(span_texts, div_scores))

            for span_text, div_score in text_score_list :
                final_text = span_text.text.strip()
                final_score = int(div_score.text)

                wr.writerow([count, final_text, final_score])
                count += 1

            print(i)

        else :
            print("요청에 실패하였습니다. (Connection failed.)")

    for i in range(1, 1001) :
        res = req.get(url2 + str(i))

        if res.status_code == 200 :
            soup = Bsoup(res.text, "html.parser")
            span_texts = soup.find_all(attrs={ "id" : re.compile("_filtered_ment_[0-9]") })
            div_scores = soup.find_all(attrs={ "class" : "star_score" })

            text_score_list = list(zip(span_texts, div_scores))

            for span_text, div_score in text_score_list :
                final_text = span_text.text.strip()
                final_score = int(div_score.text)

                wr.writerow([count, final_text, final_score])
                count += 1

            print(i)

        else :
            print("요청에 실패하였습니다. (Connection failed.)")

    for i in range(1, 1001) :
        res = req.get(url3 + str(i))

        if res.status_code == 200 :
            soup = Bsoup(res.text, "html.parser")
            td_texts = soup.find_all(attrs={ "class" : "title" })
            div_scores = soup.find_all(attrs={ "class" : "list_netizen_score" })

            text_score_list = list(zip(td_texts, div_scores))

            for td_text, div_score in text_score_list :
                final_text = td_text.text.split("\n")[5]
                final_score = int(div_score.text.replace("별점 - 총 10점 중", ""))

                wr.writerow([count, final_text, final_score])
                count += 1

            print(i)

        else :
            print("요청에 실패하였습니다. (Connection failed.)")

    """
    for i in range(1, 1001) :
        res = req.get(url3 + str(i))

        if res.status_code == 200 :
            soup = Bsoup(res.text, "html.parser")
            td_texts = soup.find_all(attrs={ "class" : "title" })
            div_scores = soup.find_all(attrs={ "class" : "list_netizen_score" })

            text_score_list = list(zip(td_texts, div_scores))

            for td_text, div_score in text_score_list :
                final_text = td_text.text.split("\n")[5]
                final_score = int(div_score.text.replace("별점 - 총 10점 중", ""))

                wr.writerow([count, final_text, final_score])
                count += 1

            print(i)

        else :
            print("요청에 실패하였습니다. (Connection failed.)")

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

    """