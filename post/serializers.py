from rest_framework import serializers
from .models import Company, JobPost, JobPostSkillSet

class CompanySerializer(serializers.ModelSerializer):
   class Meta:
        # serializer에 사용될 model, field지정
        model = Company
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["company_name", "business_area"]


class JobPostSerializer(serializers.ModelSerializer):
   class Meta:
        # serializer에 사용될 model, field지정
        model = JobPost
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["job_type", "company_id", "job_description", "salary", "created_at"]


class JobPostSkillSetSerializer(serializers.ModelSerializer):
   class Meta:
        # serializer에 사용될 model, field지정
        model = JobPostSkillSet
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["skill_set_id", "job_post_id"]