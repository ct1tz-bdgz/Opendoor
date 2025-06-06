# -*- coding: utf-8 -*-

from tests.unit import AWSMockServiceTestCase

from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion
from boto.mturk.qualification import \
     Qualifications, Requirement

QUAL_NO_ONE_ELSE_HAS_ID = "333333333333333333333333333333"

MOCK_SERVER_RESPONSE = b"""
<MockServerResponse>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</MockServerResponse>"""


class TestMTurkPostingWithQualificationsDoesnotexist(AWSMockServiceTestCase):
    connection_class = MTurkConnection

    def setUp(self):
        super(TestMTurkPostingWithQualificationsDoesnotexist, self).setUp()

    def test_qualification_doesnotexist(self):
        self.set_http_response(
            status_code=200,
            body=MOCK_SERVER_RESPONSE)
        q = ExternalQuestion(
            external_url="http://samplesite",
            frame_height=800)
        keywords = ['boto', 'test', 'doctest']
        title = "Boto External Question Test"
        annotation = 'An annotation from boto external question test'
        qualifications = Qualifications()
        test_requirement = Requirement(
                           qualification_type_id=QUAL_NO_ONE_ELSE_HAS_ID,
                           comparator='DoesNotExist')
        qualifications.add(test_requirement)
        create_hit_rs = self.service_connection.create_hit(
                        question=q,
                        lifetime=60*65,
                        max_assignments=2,
                        title=title,
                        keywords=keywords,
                        reward=0.05,
                        duration=60*6,
                        approval_delay=60*60,
                        annotation=annotation,
                        qualifications=qualifications)
        self.assert_request_parameters({
            'QualificationRequirement.1.Comparator':
                'DoesNotExist',
            'QualificationRequirement.1.QualificationTypeId':
                '333333333333333333333333333333'},
            ignore_params_values=['AWSAccessKeyId',
                                  'SignatureVersion',
                                  'Timestamp',
                                  'Title',
                                  'Question',
                                  'AssignmentDurationInSeconds',
                                  'RequesterAnnotation',
                                  'Version',
                                  'LifetimeInSeconds',
                                  'AutoApprovalDelayInSeconds',
                                  'Reward.1.Amount',
                                  'Description',
                                  'MaxAssignments',
                                  'Reward.1.CurrencyCode',
                                  'Keywords',
                                  'Operation'])
        self.assertEqual(create_hit_rs.status, True)
