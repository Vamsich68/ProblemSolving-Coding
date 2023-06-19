class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def mailformat(email):
            local, domain = email.split("@")
            temp = local.split("+")
            local=temp[0].replace('.',"")
            return local+'@'+domain
        res=set()
        for email in emails:
            res.add(mailformat(email))
        return len(res)