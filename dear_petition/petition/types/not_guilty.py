from django.db.models import Q

from dear_petition.petition.models import OffenseRecord
from dear_petition.petition.constants import DISMISSED_DISPOSITION_METHODS


def get_offense_records(batch, jurisdiction=""):
    qs = OffenseRecord.objects.filter(offense__ciprs_record__batch=batch)
    if jurisdiction:
        qs = qs.filter(offense__ciprs_record__jurisdiction=jurisdiction)
    query = Q(action="CHARGED") & Q(offense__verdict__iexact="Not Guilty")
    qs = qs.filter(query)
    return qs.select_related("offense__ciprs_record__batch")
