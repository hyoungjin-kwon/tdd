from django.test import TestCase

# Create your tests here.

class QuesitonIndexViewTests(TestCase):
  """  def test_has_ul(self):
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<ul>")
        """

  def test_has_no_question(self):
      '''
      If no question exist, an approximate message should be displayed
      '''
      response = self.client.get("/polls/")
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, "등록된 설문조사가 없습니다.")
      self.assertQuerysetEqual(response.context['question_list'],[])