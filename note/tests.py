import datetime

from django.test import TestCase
from django.utils import timezone

from .models import note

class NoteModelTest(TestCase):
    def test_was_noted_recently_with_future_question(self):
        #ตั้งเวลาการบันทึกโน้ตที่ใช้ในการ test 
        time = timezone.now() + datetime.timedelta(days=200)
        future_note = note(Pub_Date=time)
        #ถ้าเรียกใช้ was_noted_recently() output ควรจะเป็น False
        self.assertIs(future_note.was_noted_recently(),False)


