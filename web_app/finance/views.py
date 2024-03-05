from django.shortcuts import render
# Create your views here.


def finance_home(request):
    # import requests as req
    # from bs4 import BeautifulSoup
    # import time
    # import pprint
    #
    #
    # value_urls = {
    #     'DOLLAR_RUB': 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&client=safari&sca_esv=589207572&rls=en&sxsrf=AM9HkKnmnrrpGFAmm8WqX2jsR9pYU78ueQ%3A1702071065198&ei=GYtzZejjC-nNwPAPpJy12AY&ved=0ahUKEwio1OTp5ICDAxXpJhAIHSRODWsQ4dUDCA8&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiGtC00L7Qu9C70LDRgCDQuiDRgNGD0LHQu9GOMgsQABiABBixAxiDATIFEAAYgAQyChAAGIAEGBQYhwIyCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESLkgUABYwh5wA3gBkAEAmAFooAGNCaoBBDE2LjG4AQPIAQD4AQGoAhTCAgQQIxgnwgINEAAYgAQYsQMYgwEYCsICCxAuGIAEGMcBGNEDwgIPEAAYgAQYsQMYgwEYChgqwgIKEC4YgAQYigUYQ8ICCRAAGAEYgAQYCsICBxAAGIAEGArCAgkQLhgBGIAEGArCAgsQABgBGIAEGAoYKsICDxAAGAEYgAQYsQMYgwEYCsICBxAjGOoCGCfCAhYQLhgDGI8BGOUCGOoCGLQCGIwD2AEBwgIWEAAYAxiPARjlAhjqAhi0AhiMA9gBAcICERAuGIAEGLEDGIMBGMcBGNEDwgIOEC4YgAQYigUYsQMYgwHCAgsQLhiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgIKECMYgAQYigUYJ8ICChAAGIAEGIoFGEPCAhAQABiABBiKBRhDGLEDGIMBwgINEAAYgAQYigUYQxixA8ICCxAAGIAEGLEDGMkD4gMEGAAgQYgGAboGBggBEAEYCw&sclient=gws-wiz-serp',
    #     'EURO_RUB': 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&client=safari&sca_esv=588873340&rls=en&sxsrf=AM9HkKnbltYie5wtby-w6AbeFsGpP29erQ%3A1701986503446&ei=x0ByZZrvGszUwPAPsOO7kAE&ved=0ahUKEwja7sznqf6CAxVMKhAIHbDxDhIQ4dUDCA8&uact=5&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiFtC10LLRgNC-INC6INGA0YPQsdC70Y4yCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIKEAAYgAQYFBiHAjIFEAAYgARIxg9QAFjuDXAAeAGQAQCYAbkCoAGdDaoBBzcuMS4zLjG4AQPIAQD4AQHCAgQQIxgnwgIKECMYgAQYigUYJ8ICCxAAGIAEGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAhEQLhiABBixAxiDARjHARjRA8ICChAAGIAEGIoFGEPCAg0QABiABBgUGIcCGLEDwgINEAAYgAQYigUYQxixA8ICDhAuGIMBGNQCGLEDGIAEwgILEC4YgAQYxwEY0QPCAhAQABiABBiKBRhDGLEDGIMB4gMEGAAgQYgGAQ&sclient=gws-wiz-serp',
    #     'POUND_RUB': 'https://www.google.com/search?q=%D1%84%D1%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&client=safari&sca_esv=588873340&rls=en&sxsrf=AM9HkKmVtkb7l2BjZUoEELncycb7DhYaWA%3A1702072084135&ei=FI9zZbvwB7DLwPAP0fmgsAM&oq=%D1%84%D1%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5&gs_lp=Egxnd3Mtd2l6LXNlcnAiD9GE0YPQvdGCINGB0YLQtSoCCAAyDxAAGIAEGIoFGEMYRhiCAjIIEAAYgAQYsQMyChAAGIAEGIoFGEMyChAAGIAEGIoFGEMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyGxAAGIAEGIoFGEMYRhiCAhiXBRiMBRjdBNgBAUjLIFAAWOQYcAR4AZABAJgBUqAB-QWqAQIxMrgBAcgBAPgBAagCFMICChAjGIAEGIoFGCfCAhEQLhiABBixAxiDARjHARjRA8ICCxAAGIAEGLEDGIMBwgIKEAAYgAQYFBiHAsICEBAAGIAEGIoFGEMYsQMYgwHCAhAQABgBGIAEGAoYKhhGGPkBwgIJEAAYARiABBgKwgIHEAAYgAQYCsICJxAAGAEYgAQYChgqGEYY-QEYlwUYjAUY3QQYRhj0Axj1Axj2A9gBAcICDRAAGIAEGIoFGEMYsQPCAgoQABiABBixAxgKwgIHECMY6gIYJ8ICExAAGIAEGIoFGEMY6gIYtALYAQLCAgQQIxgnwgIOEC4YgAQYigUYsQMYgwHCAg0QLhiABBiKBRhDGNQCwgISEAAYgAQYigUYQxixAxhGGIICwgIOEAAYgAQYigUYsQMYgwHCAh4QABiABBiKBRhDGLEDGEYYggIYlwUYjAUY3QTYAQHiAwQYACBBiAYBugYGCAEQARgTugYGCAIQARgB&sclient=gws-wiz-serphttps://www.google.com/search?q=%D1%84%D1%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&client=safari&sca_esv=588873340&rls=en&sxsrf=AM9HkKmVtkb7l2BjZUoEELncycb7DhYaWA%3A1702072084135&ei=FI9zZbvwB7DLwPAP0fmgsAM&oq=%D1%84%D1%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5&gs_lp=Egxnd3Mtd2l6LXNlcnAiD9GE0YPQvdGCINGB0YLQtSoCCAAyDxAAGIAEGIoFGEMYRhiCAjIIEAAYgAQYsQMyChAAGIAEGIoFGEMyChAAGIAEGIoFGEMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyGxAAGIAEGIoFGEMYRhiCAhiXBRiMBRjdBNgBAUjLIFAAWOQYcAR4AZABAJgBUqAB-QWqAQIxMrgBAcgBAPgBAagCFMICChAjGIAEGIoFGCfCAhEQLhiABBixAxiDARjHARjRA8ICCxAAGIAEGLEDGIMBwgIKEAAYgAQYFBiHAsICEBAAGIAEGIoFGEMYsQMYgwHCAhAQABgBGIAEGAoYKhhGGPkBwgIJEAAYARiABBgKwgIHEAAYgAQYCsICJxAAGAEYgAQYChgqGEYY-QEYlwUYjAUY3QQYRhj0Axj1Axj2A9gBAcICDRAAGIAEGIoFGEMYsQPCAgoQABiABBixAxgKwgIHECMY6gIYJ8ICExAAGIAEGIoFGEMY6gIYtALYAQLCAgQQIxgnwgIOEC4YgAQYigUYsQMYgwHCAg0QLhiABBiKBRhDGNQCwgISEAAYgAQYigUYQxixAxhGGIICwgIOEAAYgAQYigUYsQMYgwHCAh4QABiABBiKBRhDGLEDGEYYggIYlwUYjAUY3QTYAQHiAwQYACBBiAYBugYGCAEQARgTugYGCAIQARgB&sclient=gws-wiz-serp',
    #     'SWISSFRANK_RUB': 'https://www.google.com/search?q=%D1%88%D0%B2%D0%B5%D0%B9%D1%86%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9+%D1%84%D1%80%D0%B0%D0%BD%D0%BA+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&client=safari&sca_esv=588873340&rls=en&sxsrf=AM9HkKnqSayGKpFereDffsXM5cnwI6HO3Q%3A1702072141369&ei=TY9zZZKRFo6zwPAP8uSa2AY&oq=%D0%A8%D0%B2%D0%B5%D0%B9%D1%86%D0%B0&gs_lp=Egxnd3Mtd2l6LXNlcnAiDNCo0LLQtdC50YbQsCoCCAAyDxAAGIAEGIoFGEMYRhiCAjINEAAYgAQYigUYQxixAzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIIEC4YgAQYsQMyChAAGIAEGIoFGEMyGxAAGIAEGIoFGEMYRhiCAhiXBRiMBRjdBNgBAUitJlAAWOkbcAV4AZABAJgBVqABwAaqAQIxMbgBAcgBAPgBAagCFMICChAjGIAEGIoFGCfCAgQQIxgnwgILEAAYgAQYsQMYgwHCAgUQABiABMICCBAAGIAEGLEDwgIQEC4YgAQYigUYQxjHARjRA8ICCxAAGAEYgAQYChgqwgIJEAAYARiABBgKwgIJEC4YARiABBgKwgIQEAAYARiABBgKGCoYRhiCAsICDxAuGAEYgAQYxwEYrwEYCsICHBAAGAEYgAQYChgqGEYYggIYlwUYjAUY3QTYAQHCAgcQIxjqAhgnwgITEAAYgAQYigUYQxjqAhi0AtgBAsICDhAuGIAEGIoFGLEDGIMBwgIOEC4YgAQYsQMYxwEYrwHCAgsQLhiABBixAxiDAcICBRAuGIAEwgIIEC4Y1AIYgATiAwQYACBBiAYBugYGCAEQARgTugYGCAIQARgB&sclient=gws-wiz-serp',
    #     'CHINAUAN_RUB': 'https://www.google.com/search?q=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9%D1%81%D0%BA%D0%B8%D0%B9+%D1%8E%D0%B0%D0%BD%D1%8C+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&client=safari&sca_esv=589207572&rls=en&sxsrf=AM9HkKn_cfV7JQr0ZQu5l_H6RKMonJSv_g%3A1702071199964&ei=n4tzZZ-5OtytwPAP3-6n0AQ&oq=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9&gs_lp=Egxnd3Mtd2l6LXNlcnAiCtC60LjRgtCw0LkqAggBMg8QABiABBiKBRhDGEYYggIyChAAGIAEGIoFGEMyDRAAGIAEGIoFGEMYsQMyChAAGIAEGIoFGEMyDRAAGIAEGIoFGEMYsQMyChAAGIAEGIoFGEMyChAAGIAEGIoFGEMyDRAuGIAEGIoFGEMYsQMyChAAGIAEGIoFGEMyChAuGIAEGIoFGEMyGxAAGIAEGIoFGEMYRhiCAhiXBRiMBRjdBNgBA0jguwtQAFiBrQtwBXgAkAEAmAFVoAGbBqoBAjEyuAEByAEA-AEBqAIUwgIHECMY6gIYJ8ICExAAGIAEGIoFGEMY6gIYtALYAQHCAhQQABiABBjjBBjpBBjqAhi0AtgBAcICBBAjGCfCAg0QABiABBixAxiDARgKwgIFEAAYgATCAgsQLhiABBjHARjRA8ICEBAAGAEYgAQYigUYQxgKGCrCAgkQABgBGIAEGArCAgcQABiABBgKwgIJEC4YARiABBgKwgIKECMYgAQYigUYJ8ICDRAAGIAEGBQYhwIYsQPCAgsQABiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgIIEC4YgAQYsQPCAgsQLhiABBixAxiDAcICDhAuGIAEGLEDGMcBGNEDwgIREC4YgAQYsQMYgwEYxwEY0QPCAhYQLhiABBiKBRhDGLEDGIMBGMcBGNEDwgIQEAAYgAQYigUYQxixAxiDAcICDhAAGAEYgAQYigUYQxgKwgIIEAAYgAQYsQPCAiUQLhiABBiKBRhDGLEDGIMBGMcBGNEDGJcFGNwEGN4EGOAE2AECwgIQEAAYgAQYFBiHAhixAxiDAcICChAAGIAEGBQYhwLiAwQYACBBiAYBugYGCAEQARgBugYGCAIQARgUugYGCAMQARgT&sclient=gws-wiz-serp',
    #     'JAPANIENA_RUB': 'https://www.google.com/search?q=%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%B8%D0%B5%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&client=safari&sca_esv=589207572&rls=en&sxsrf=AM9HkKm8f5-picRyQwMOEYGVPM2o7dmVSw%3A1702072211828&ei=k49zZZOZMrOxwPAP9PKUuAc&oq=%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%B8%D0%B5%D0%BD%D0%B0%C2%A0&gs_lp=Egxnd3Mtd2l6LXNlcnAiG9GP0L_QvtC90YHQutCw0Y8g0LjQtdC90LDCoCoCCAAyChAAGIAEGBQYhwIyBRAAGIAEMgoQABiABBgUGIcCMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEj7JlAAWN8ecAJ4AZABAJgBYKABmwmqAQIxNrgBAcgBAPgBAagCFMICCxAAGIAEGLEDGIMBwgIIEAAYgAQYsQPCAhEQLhiABBixAxiDARjHARjRA8ICDhAuGIAEGLEDGMcBGNEDwgILEC4YgAQYsQMYgwHCAgcQIxjqAhgnwgITEAAYgAQYigUYQxjqAhi0AtgBAcICChAjGIAEGIoFGCfCAgoQABiABBiKBRhDwgIPEAAYgAQYigUYQxhGGIICwgINEAAYgAQYigUYQxixA8ICERAAGIAEGIoFGLEDGIMBGMkDwgIbEAAYgAQYigUYQxhGGIICGJcFGIwFGN0E2AECwgILEAAYgAQYigUYkgPCAg0QABiABBgUGIcCGLEDwgIOEC4YgAQYigUYsQMYgwHCAggQLhjUAhiABMICCBAuGIAEGLED4gMEGAAgQYgGAboGBggBEAEYAboGBggCEAEYEw&sclient=gws-wiz-serp',
    #     'LIRA_RUN': 'https://www.google.com/search?q=%D0%BB%D0%B8%D1%80%D0%B0+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&client=safari&sca_esv=589207572&rls=en&sxsrf=AM9HkKlsltmaLRX-dpTz1HVXyKvDfDS-bA%3A1702072248743&ei=uI9zZZCCLfDhwPAP4tG0iAY&ved=0ahUKEwiQvpKe6YCDAxXwMBAIHeIoDWEQ4dUDCA8&uact=5&oq=%D0%BB%D0%B8%D1%80%D0%B0+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&gs_lp=Egxnd3Mtd2l6LXNlcnAiE9C70LjRgNCwINGA0YPQsdC70YwyDRAAGIAEGLEDGEYYggIyBRAAGIAEMgoQABiABBgUGIcCMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIZEAAYgAQYsQMYRhiCAhiXBRiMBRjdBNgBA0iRGVDEAlj1FnADeAGQAQGYAbECoAHTCKoBBjExLjMtMbgBA8gBAPgBAagCFMICBxAjGOoCGCfCAhMQABiABBiKBRhDGOoCGLQC2AEBwgIWEC4YAxiPARjlAhjqAhi0AhiMA9gBAsICFhAAGAMYjwEY5QIY6gIYtAIYjAPYAQLCAgoQIxiABBiKBRgnwgIEECMYJ8ICDhAAGIAEGIoFGLEDGIMBwgIEEAAYA8ICCxAAGIAEGLEDGIMBwgIOEC4YgAQYsQMYxwEY0QPCAhEQLhiDARjHARixAxjRAxiABMICERAuGIAEGLEDGIMBGMcBGK8BwgIREC4YgAQYsQMYgwEYxwEY0QPCAg0QABiABBiKBRhDGLEDwgIKEAAYgAQYigUYQ8ICChAuGIAEGIoFGEPCAggQABiABBixA8ICDRAAGIAEGBQYhwIYsQPiAwQYACBBiAYBugYGCAEQARgBugYGCAIQARgLugYGCAMQARgT&sclient=gws-wiz-serp',
    #     'TENGE_RUN': 'https://www.google.com/search?q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&client=safari&sca_esv=589207572&rls=en&sxsrf=AM9HkKl-NagjkWv7iQHbytCeCkKdr0gTWQ%3A1702072288488&ei=4I9zZeO5HfquwPAPlJSE6AM&ved=0ahUKEwjjqYyx6YCDAxV6FxAIHRQKAT0Q4dUDCA8&uact=5&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&gs_lp=Egxnd3Mtd2l6LXNlcnAiFdGC0LXQvdCz0LUg0YDRg9Cx0LvRjDISEAAYgAQYigUYQxixAxhGGIICMg0QABiABBiKBRhDGLEDMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyHhAAGIAEGIoFGEMYsQMYRhiCAhiXBRiMBRjdBNgBAUjcGFAAWKYXcAR4AZABAJgBrgGgAeIIqgEEMTQuMbgBA8gBAPgBAagCFMICChAjGIAEGIoFGCfCAgsQABiABBixAxiDAcICCxAuGIAEGMcBGNEDwgIOEC4YgAQYsQMYxwEY0QPCAhEQLhiABBixAxiDARjHARjRA8ICCxAuGIAEGMcBGK8BwgIIEAAYgAQYsQPCAggQLhiABBixA8ICCxAAGAEYgAQYChgqwgIJEAAYARiABBgKwgIMEAAYARiABBixAxgKwgIQEAAYARiABBgKGCoYRhiCAsICBxAAGIAEGArCAhwQABgBGIAEGAoYKhhGGIICGJcFGIwFGN0E2AEBwgIHECMY6gIYJ8ICExAAGIAEGIoFGEMY6gIYtALYAQLCAgoQABiABBiKBRhDwgIREC4YgwEYxwEYsQMY0QMYgATCAgQQIxgnwgINEAAYgAQYFBiHAhixA8ICEhAAGIAEGBQYhwIYsQMYRhiCAsICHhAAGIAEGBQYhwIYsQMYRhiCAhiXBRiMBRjdBNgBAeIDBBgAIEGIBgG6BgYIARABGBO6BgYIAhABGAE&sclient=gws-wiz-serp',
    #     'LIPARIT_RUB': 'https://www.google.com/search?q=%D0%B0%D1%80%D0%BC%D1%8F%D0%BD%D1%81%D0%BA%D0%B8%D0%B9+%D0%B4%D1%80%D0%B0%D0%BC+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&client=safari&sca_esv=589207572&rls=en&sxsrf=AM9HkKnwZm0C6bU-ISltNjLmOH0MVjAV0g%3A1702072313312&ei=-Y9zZevZEqGwwPAPouyKwAs&oq=%D0%B0%D1%80%D1%8F%D0%BC%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%C2%A0&gs_lp=Egxnd3Mtd2l6LXNlcnAiFNCw0YDRj9C80L3RgdC60LjQucKgKgIIATIPEAAYgAQYigUYQxhGGIICMgoQABiABBiKBRhDMgoQABiABBiKBRhDMg0QABiABBiKBRhDGLEDMgoQABiABBiKBRhDMgoQABiABBiKBRhDMgoQABiABBixAxgKMgoQABiABBixAxgKMgoQLhiABBixAxgKMgoQABiABBixAxgKSMYeUABYhxRwA3gBkAEAmAFcoAHhB6oBAjEzuAEByAEA-AEBqAIUwgIKECMYgAQYigUYJ8ICDBAjGIAEGIoFGBMYJ8ICERAuGIAEGLEDGIMBGMcBGNEDwgILEAAYgAQYsQMYgwHCAg4QLhiABBixAxiDARjUAsICCxAAGAEYgAQYChgqwgIKEC4YsQMYgAQYCsICCxAuGIAEGMcBGK8BwgIFEAAYgATCAgkQABgBGIAEGArCAgcQLhiABBgKwgIHECMY6gIYJ8ICExAAGIAEGIoFGEMY6gIYtALYAQHCAgQQIxgnwgINEC4YgAQYigUYQxixA8ICDhAAGIAEGIoFGLEDGIMBwgIQEC4YgAQYigUYQxixAxiDAcICBxAAGIAEGArCAg0QLhiABBjHARivARgKwgIFEC4YgATCAgwQABiABBgKGEYYggLCAhAQLhiABBixAxjHARjRAxgKwgIYEAAYgAQYChhGGIICGJcFGIwFGN0E2AECwgIbEAAYgAQYigUYQxhGGIICGJcFGIwFGN0E2AEC4gMEGAAgQYgGAboGBggBEAEYAboGBggCEAEYEw&sclient=gws-wiz-serp',
    #     'BELRUB_RUB': 'https://www.google.com/search?q=%D0%B1%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9+%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&client=safari&sca_esv=589207572&rls=en&sxsrf=AM9HkKlPXG605LHfv5dmaOLUAw-4tsTIlQ%3A1702072375943&ei=N5BzZZ6TObqNwPAPr4u8iAg&ved=0ahUKEwjeiuba6YCDAxW6BhAIHa8FD4EQ4dUDCA8&uact=5&oq=%D0%B1%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9+%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&gs_lp=Egxnd3Mtd2l6LXNlcnAiL9Cx0LXQu9C-0YDRg9GB0YHQutC40Lkg0YDRg9Cx0LvRjCDQuiDRgNGD0LHQu9GMMgUQABiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHkiUDlDNAVinDHABeAGQAQCYAZ4BoAGZBaoBAzguMbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIKECMYgAQYigUYJ8ICCBAAGIAEGMsBwgIPECMYgAQYigUYJxhGGIICwgIZEAAYgAQYigUYRhiCAhiXBRiMBRjdBNgBAcICChAAGIAEGBQYhwLiAwQYACBBiAYBkAYKugYGCAEQARgT&sclient=gws-wiz-serp'
    # }
    #
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',}
    #
    # def get_currency_price(url, headers):
    #     full_page = req.get(url, headers=headers)
    #     soup = BeautifulSoup(full_page.content, 'html.parser')
    #
    #     convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    #
    #     return convert[0].text
    #
    # def to_data(value_urls=value_urls, headers=headers):
    #     data = dict()
    #     for cur in value_urls:
    #         data[cur] = get_currency_price(value_urls[cur], headers)
    #     return data
    #

    # data = to_data(value_urls, headers)

    data = {}



    return render(request, 'finance/finance_dashboard.html', context=data)

def visualize(request):
    return render(request, 'finance/visualization_dashboard.html')


def analytics(request):
    return render(request, 'finance/analytics_dashboard.html')

def analytics_sber(request):
    return render(request, 'analytics/sber.html')