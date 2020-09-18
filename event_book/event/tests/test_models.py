from django.test import TestCase

import pytest
from events.models import Event,


@pytest.mark.django_db
def test_event_model(event, category, account):
    assert event.details == 'For Python developers'
    assert event.name == 'Pycon'
    assert event.venue == 'jand'
    assert event.creator == account
    assert event.category == category
    assert event.get_number_of_attendees() == 0
    assert event.get_comments_number() == 0
