base_headers = {
    "Host": "api.nike.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.nike.com/launch/t/air-jordan-3-laser-orange?size=11&productId=b106cd63-8b49-5365-b48d-2ea96a1fce52",
    "Origin": "https://www.nike.com",
    "Connection": "keep-alive",
    "TE": "Trailers",
}

r = requests.options(
    "https://api.nike.com/buy/checkout_previews/v2/0619eb39-3b63-4058-856e-016014eb6ccc",
    headers={
        **base_headers,
        "Accept": "*/*",
        "Access-Control-Request-Method": "PUT",
        "Access-Control-Request-Headers": "appid,authorization,content-type,x-b3-parentspanid,x-b3-spanid,x-b3-traceid",
    },
)


r = requests.put(
    "https://api.nike.com/buy/checkout_previews/v2/0619eb39-3b63-4058-856e-016014eb6ccc",
    cookies={
        "AnalysisUserId": "67.220.142.73.147921597985814847",
        "feature_tests": "as_esi_noop_test:variation_2",
        "feature_enabled__as_esi_noop": "true",
        "audience_segmentation_performed": "true",
        "geoloc": "cc=US,rc=LA,tp=vhigh,tz=CST,la=30.2894,lo=-93.0808",
        "AMCV_F0935E09512D2C270A490D4D@AdobeOrg": "1994364360|MCMID|12052267867967813364661667887273631341|MCAID|NONE|MCOPTOUT-1597992877s|NONE|vVersion|3.4.0",
        "_abck": "ED14177F3A85EBAABD77FEDB38E32236~-1~YAAQXgXorAsDXOhzAQAAkYtVEQRHAXWfFkYlBaI8UCvuzB9NUUy/hjm36EB3nv0cW++GqMvVizYjhevYpC3pQ79UuQvoouoK+FJAT4Km7L4TF5HQ1K0bH4ivv+U7FjYkYM6NT3NNNtXNMAmws2QG3QzcvuC0tzlZ4PGsbE5JioKVf16nCDraoUHyA62nzWvGDYBv6hi7ppXohlPuz+dSzZxkkz8oRhIKdMsVHEALwRrId50lCbwZhHIaC9RrsmfAyNb9iA/Njj7YND6IM06BlF4frU1P5rQJ2qYKkW/yKCxe7s6Qboq027yCjmV9qjlnpEfQjViTpedf4uQWJm+pWDy35/9a1O6zkg/HIlJGl3s=~0~-1~-1",
        "s_ecid": "MCMID|12052267867967813364661667887273631341",
        "NIKE_COMMERCE_COUNTRY": "US",
        "NIKE_COMMERCE_LANG_LOCALE": "en_US",
        "nike_locale": "us/en_us",
        "cid": "undefined|undefined",
        "optimizelyEndUserId": "oeu1597985676967r0.998616183752938",
        "_gcl_au": "1.1.16627685.1597985677",
        "AMCVS_F0935E09512D2C270A490D4D@AdobeOrg": "1",
        "RT": '"z=1&dm=nike.com&si=3643dd17-b7be-420b-806c-7a9f2c5b91af&ss=ke4ale9k&sl=8&tt=7tv&bcn=//173e2529.akstat.io/&ld=d69u&nu=3tacntmj&cl=820b"',
        "anonymousId": "1DBD5527E8DD82B6FDFB01FDA6ACD1D8",
        "ppd": "checkout|snkrs>checkout>order review",
        "cto_bundle": "F8UaKV9mTiUyQlpvejRFSHpsV2FNbUk1eDNQVkRiR21sQW1SdVZyMXBRWjlIYzhTT1YlMkZBZ3h2SldqZ1N6cmV0SGJYZEU3cmpQRTVxUDVHWjFJVzlYaUtkYm1CWjBFZVpESkJ0VVcxRGZIa1NDMUFxb3E3VzgyaEEyaFlEbWUlMkY3Tm55N3ZqRm04ZEVMTTZDUk1Yd1ZlZVhZUXZTMGclM0QlM0Q",
        "fs_uid": "rs.fullstory.com#BM7A6#5396653203996672:5883671616897024/1629521678",
        "_ga": "GA1.2.228017437.1597985679",
        "_gid": "GA1.2.39270780.1597985679",
        "CONSUMERCHOICE": "us/en_us",
        "NIKE_CART": "b:c",
        "siteCatalyst_sample": "78",
        "dreamcatcher_sample": "11",
        "neo_sample": "54",
        "guidU": "46555eb9-52e4-45d6-9837-ed9b06ce7517",
        "sq": "3",
        "bc_nike_triggermail": '{"distinct_id": "1740f5e5fcb625-0010fe33633bc3-4c302273-1fa400-1740f5e5fcc65e","cart_total": 0}',
        "AKA_A2": "A",
        "ak_bmsc": "ADBC47D005FAE0F322DB37FF55C6187417CA334E113A0000F1D13F5FE6FC2E05~plfTX3WAonCUc6fg9SPzKVkMlgxiWVRoRgxRSBlCIaOCRBzwaII6Tjq/r4f+gWeEAp41SeSZZjIh4G2tvTUyZDdG3Zr+6MBBlLBGctG+ER/g7n/+pOjo76bgyBebE2v6lefKWiz71f1SSV42VqZtbn4wvAPgOnfgLV/jCclsyAB6VAXQ/WPWLkyvlC4ZjAblCXqUY1+jRN6rMZlzLVCcqnxHyCem0fZCQsmQ17finNILoPKuRrgGRxVuJwM0MfJq2s",
        "bm_sz": "32E0C1E2700898AE4F7BBFDE2C9D1D1B~YAAQTjPKFzQULuZzAQAAeBdMEQhrlQYggpIkGFBSbjrIW/chMzpJQaAUX+NLaE8cGev7uhBkMx1Qsd28X9UR8ucNHtNnuINZkMdoS6cwec0V37IOtUBQfG0ZmemK1x2kRvLX1jeJeOgDpnGdHR4XkUJXeJhBTTmOkXv4BZJ+qLCNFO9wnOlJHXom8/cX",
        "bm_sv": "3DA3E2166D7D4EFDFE5A39F7ABAAB294~YqGFNUbnXPqPH7eY/AOUy5VQYBe5WZ0SvYR5Fjh7w9xpDtpgQvXRt2A7lS3yHkyq8qRaAeMonJqktHBZtSXfiiIzettCMwWni+3G+vhcrlvz7+JH3rRgMS/X4R7hOdbxBT6rHmAbT9p9LdP0qQSvRY03c9D9GxEfd4x8FMdZHec=",
        "guidS": "e3dd8a7f-ea35-4e00-e4f4-38f77896bf64",
        "guidSTimestamp": "1598017896799|1598018220075",
        "slCheck": "10/HYK9s9BauGpqW50MH3w5DRJ5h872W+3EapolLKWYiHeqc+8BN5kyUP4JKfYq41UVSoXGw1+Z4IGOgZ9h0ymt0de8/uezcq1OM4QtJMTFEiG1APadulJ8ujDh3Vy7H",
        "lls": "3",
        "llCheck": "2aqK38EZzbUkhA3fHp3+uesD8p8isqovwNhxnwvco8bfYPfEhNjkTOIPGyRGtjNgJDxPz3qefEM+aqEQ64bw/p+n1XW25YLRXmv/8NZn42sOmhMo7iNlhrLD2yMqomrH1lg5FWVCGPqCELysliw02avcS4lfoEhPYzdAyHp9UcA=",
        "sls": "3",
        "co_size": "11",
        "_uetsid": "c9ec9995cda83258f21690f452c14f04",
        "_uetvid": "5de7d4ba983f8d2e18832d7b41432ab4",
    },
    headers={
        **base_headers,
        "Accept": "application/json",
        "appid": "com.nike.commerce.snkrs.web",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImFlYmJkMWMyLTNjNDUtNDM5NS04MGMzLWE3YTIyMmJlOTJmMHNpZyJ9.eyJ0cnVzdCI6MTAwLCJpYXQiOjE1OTgwMTgwODUsImV4cCI6MTU5ODAyMTY4NSwiaXNzIjoib2F1dGgyYWNjIiwianRpIjoiNmUwYjdmYjctZTJjZC00ZWU3LThkNjgtMGZiZjlkMTZhNmY4IiwibGF0IjoxNTk4MDE4MDg1LCJhdWQiOiJjb20ubmlrZS5kaWdpdGFsIiwic3ViIjoiY29tLm5pa2UuY29tbWVyY2Uuc25rcnMud2ViIiwic2J0IjoibmlrZTphcHAiLCJzY3AiOlsiY29tbWVyY2UiXSwicHJuIjoiMjVmY2RmOGYtMWZkNS00YTc1LWFmOWItZGYzMjRkNjA0OGJiIiwicHJ0IjoibmlrZTpwbHVzIn0.v36lJsUNmRCrvppOzDpojMpcePBlpn_xn56AX6XR2FVc0EXGa4IxFNfP9n1gdQ3NKMAnAmIGvYWZCBoqGQzwHxSaNAzxH2cIb3Po3SKaBaJ-D1CR8aqdHlZAXhjY-AJ56m-auagkGfDl1PWIPiz0ltc-JSDybFwE-9-3nuATv3lkfS7e3vsDiLsWwM-qDIHGyinYdkX8eYQtjpL1o97LhrYlC0jJqW28wsXgL2eXjqspLeXTbk9T78X43Q4oGJ86jpabZhR19J8Eqntg7D3UEHcuPHZ4N0cy-9XrRd9luE7webZ2XxicqthG63AQ2WnhHpujT7dhzLzAnAyc6nhYwQ",
        "X-B3-TraceId": "03754d0c80a05977",
        "X-B3-SpanId": "6281796aaaa98173",
        "X-B3-ParentSpanId": "d84a120f48343d24",
        "Cookie": 'AnalysisUserId=67.220.142.73.147921597985814847; feature_tests=as_esi_noop_test:variation_2; feature_enabled__as_esi_noop=true; audience_segmentation_performed=true; geoloc=cc=US,rc=LA,tp=vhigh,tz=CST,la=30.2894,lo=-93.0808; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C12052267867967813364661667887273631341%7CMCAID%7CNONE%7CMCOPTOUT-1597992877s%7CNONE%7CvVersion%7C3.4.0; _abck=ED14177F3A85EBAABD77FEDB38E32236~-1~YAAQXgXorAsDXOhzAQAAkYtVEQRHAXWfFkYlBaI8UCvuzB9NUUy/hjm36EB3nv0cW++GqMvVizYjhevYpC3pQ79UuQvoouoK+FJAT4Km7L4TF5HQ1K0bH4ivv+U7FjYkYM6NT3NNNtXNMAmws2QG3QzcvuC0tzlZ4PGsbE5JioKVf16nCDraoUHyA62nzWvGDYBv6hi7ppXohlPuz+dSzZxkkz8oRhIKdMsVHEALwRrId50lCbwZhHIaC9RrsmfAyNb9iA/Njj7YND6IM06BlF4frU1P5rQJ2qYKkW/yKCxe7s6Qboq027yCjmV9qjlnpEfQjViTpedf4uQWJm+pWDy35/9a1O6zkg/HIlJGl3s=~0~-1~-1; s_ecid=MCMID%7C12052267867967813364661667887273631341; NIKE_COMMERCE_COUNTRY=US; NIKE_COMMERCE_LANG_LOCALE=en_US; nike_locale=us/en_us; cid=undefined%7Cundefined; optimizelyEndUserId=oeu1597985676967r0.998616183752938; _gcl_au=1.1.16627685.1597985677; AMCVS_F0935E09512D2C270A490D4D%40AdobeOrg=1; RT="z=1&dm=nike.com&si=3643dd17-b7be-420b-806c-7a9f2c5b91af&ss=ke4ale9k&sl=8&tt=7tv&bcn=%2F%2F173e2529.akstat.io%2F&ld=d69u&nu=3tacntmj&cl=820b"; anonymousId=1DBD5527E8DD82B6FDFB01FDA6ACD1D8; ppd=checkout|snkrs>checkout>order%20review; cto_bundle=F8UaKV9mTiUyQlpvejRFSHpsV2FNbUk1eDNQVkRiR21sQW1SdVZyMXBRWjlIYzhTT1YlMkZBZ3h2SldqZ1N6cmV0SGJYZEU3cmpQRTVxUDVHWjFJVzlYaUtkYm1CWjBFZVpESkJ0VVcxRGZIa1NDMUFxb3E3VzgyaEEyaFlEbWUlMkY3Tm55N3ZqRm04ZEVMTTZDUk1Yd1ZlZVhZUXZTMGclM0QlM0Q; fs_uid=rs.fullstory.com#BM7A6#5396653203996672:5883671616897024/1629521678; _ga=GA1.2.228017437.1597985679; _gid=GA1.2.39270780.1597985679; CONSUMERCHOICE=us/en_us; NIKE_CART=b:c; siteCatalyst_sample=78; dreamcatcher_sample=11; neo_sample=54; guidU=46555eb9-52e4-45d6-9837-ed9b06ce7517; sq=3; bc_nike_triggermail=%7B%22distinct_id%22%3A%20%221740f5e5fcb625-0010fe33633bc3-4c302273-1fa400-1740f5e5fcc65e%22%2C%22cart_total%22%3A%200%7D; AKA_A2=A; ak_bmsc=ADBC47D005FAE0F322DB37FF55C6187417CA334E113A0000F1D13F5FE6FC2E05~plfTX3WAonCUc6fg9SPzKVkMlgxiWVRoRgxRSBlCIaOCRBzwaII6Tjq/r4f+gWeEAp41SeSZZjIh4G2tvTUyZDdG3Zr+6MBBlLBGctG+ER/g7n/+pOjo76bgyBebE2v6lefKWiz71f1SSV42VqZtbn4wvAPgOnfgLV/jCclsyAB6VAXQ/WPWLkyvlC4ZjAblCXqUY1+jRN6rMZlzLVCcqnxHyCem0fZCQsmQ17finNILoPKuRrgGRxVuJwM0MfJq2s; bm_sz=32E0C1E2700898AE4F7BBFDE2C9D1D1B~YAAQTjPKFzQULuZzAQAAeBdMEQhrlQYggpIkGFBSbjrIW/chMzpJQaAUX+NLaE8cGev7uhBkMx1Qsd28X9UR8ucNHtNnuINZkMdoS6cwec0V37IOtUBQfG0ZmemK1x2kRvLX1jeJeOgDpnGdHR4XkUJXeJhBTTmOkXv4BZJ+qLCNFO9wnOlJHXom8/cX; bm_sv=3DA3E2166D7D4EFDFE5A39F7ABAAB294~YqGFNUbnXPqPH7eY/AOUy5VQYBe5WZ0SvYR5Fjh7w9xpDtpgQvXRt2A7lS3yHkyq8qRaAeMonJqktHBZtSXfiiIzettCMwWni+3G+vhcrlvz7+JH3rRgMS/X4R7hOdbxBT6rHmAbT9p9LdP0qQSvRY03c9D9GxEfd4x8FMdZHec=; guidS=e3dd8a7f-ea35-4e00-e4f4-38f77896bf64; guidSTimestamp=1598017896799|1598018220075; slCheck=10/HYK9s9BauGpqW50MH3w5DRJ5h872W+3EapolLKWYiHeqc+8BN5kyUP4JKfYq41UVSoXGw1+Z4IGOgZ9h0ymt0de8/uezcq1OM4QtJMTFEiG1APadulJ8ujDh3Vy7H; lls=3; llCheck=2aqK38EZzbUkhA3fHp3+uesD8p8isqovwNhxnwvco8bfYPfEhNjkTOIPGyRGtjNgJDxPz3qefEM+aqEQ64bw/p+n1XW25YLRXmv/8NZn42sOmhMo7iNlhrLD2yMqomrH1lg5FWVCGPqCELysliw02avcS4lfoEhPYzdAyHp9UcA=; sls=3; co_size=11; _uetsid=c9ec9995cda83258f21690f452c14f04; _uetvid=5de7d4ba983f8d2e18832d7b41432ab4',
    },
)
