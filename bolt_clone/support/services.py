def format_article_text_for_ajax(article):
    formatted_content = " ".join(article.article_text.split()[:20]).strip(":")
    if not formatted_content[-1].isalnum():
        formatted_content = formatted_content[:-1]
    return formatted_content


def handle_ajax_request(result_query, model):
    if result_query:
        articles = model.objects.filter(article_title__icontains=result_query)
        data = [{
            "title": article.article_title,
            "content": format_article_text_for_ajax(article),
            "category": article.article_category.category_title,
            "url": article.get_absolute_url()
        } for article in articles]
    else:
        data = {}
    return data
