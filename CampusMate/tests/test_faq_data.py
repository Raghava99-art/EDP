from app.utils.data_loader import load_faqs

def test_faq_data_has_required_fields():
    faqs = load_faqs()
    assert len(faqs) >= 10
    for faq in faqs:
        assert faq["id"] != ""
        assert faq["category"] != ""
        assert faq["question"] != ""
        assert faq["answer"] != ""
