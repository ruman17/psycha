from django.db import models
from jsonfield import JSONField
import collections
from django.utils import timezone


class QResponses(models.Model):
    pub_date = models.DateTimeField(default=timezone.now,null=True, blank=True)
    response_array = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict},null=True, blank=True)
    p_f_name = models.CharField(max_length=100, blank=True, null=True)
    p_l_name = models.CharField(max_length=100, blank=True, null=True)
    p_dob = models.DateTimeField(auto_now_add=False, blank=True, null=True)