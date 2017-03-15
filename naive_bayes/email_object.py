# -*- coding: ascii -*-
import email
import io
import chardet
import sys
if sys.version_info[0] < 3:
    from BeautifulSoup import BeautifulSoup
else:
    from bs4 import BeautifulSoup

class EmailObject:
  CLRF = "\n\r\n\r"
  def __init__(self, file, category = None):
    self.file = file
    self.category = category
    self.maxDiff = None
    self.mail_body = self.file.read()
    self.mail = email.message_from_string(self.mail_body)
    self.file.close()

  def subject(self):
    return self.mail.get('Subject')

  def body(self):
    payload = self.mail.get_payload()
    parts = []
    if self.mail.is_multipart():
      parts = [self.single_body(part) for part in list(payload)]
    else:
      parts = [str(self.single_body(self.mail))]
    return self.CLRF.join(parts)
      
  def single_body(self, part):
    content_type = part.get_content_type()
    body = part.get_payload(decode=True)

    if content_type == 'text/html':
      return BeautifulSoup(body, "html.parser").text 
    elif content_type == 'text/plain':
      return body.decode('ascii', 'ignore')
    else:
      return ''
