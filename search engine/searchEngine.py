import requests
from bs4 import BeautifulSoup

class SearchEngine:
    def __init__(self):
        self.documents = {}
        self.stop_words=['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very',
                        'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 
                        'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until',
                        'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this',
                        'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at',
                        'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'or,', 'will', 'on', 'does', 'yourselves', 'then', 'that', 
                        'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where',
                        'too', 'only','myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 
                        'by','doing', 'it','how', 'further', 'was', 'here', 'than',]
        
    def get_document_from_url(self, url):
        #Requests data from the given URL and stores it in the page variable 
        page = requests.get(url)
        # print(page.status_code)
        if(page.status_code==404):
            raise ValueError
        else:
            #Uses BeautfulSoup to parser HTML code, which is then stored in the soup variable    
            soup = BeautifulSoup(page.content, 'html.parser')
            #Finds all paragraphs within the parsed HTML content  
            paragraphs = soup.findAll('p') 
            #Joins the first two paragraphs with new line character and stores it in first two paragraphs        
            first_two_paragraphs = '\n'.join([p.get_text() for p in paragraphs[2:4]])        
            #returns first two paragraphs' text                                            
            return first_two_paragraphs
    
    def add_document(self, url):
        # 'https://en.wikipedia.org/wiki/Koala
        # .spit(separator,maxsplit)
        doc_id = url.split('wiki/',1)[1] #["https://en.wikipedia.org/","Koala"]
        # doc_id1 = url.split("/",4)[-1] #['https:', '', 'en.wikipedia.org', 'wiki', 'Koala']
        try:       
            f2p_words = (self.get_document_from_url(url)).split()
            without_stopWords  = [word for word in f2p_words if word.lower() not in self.stop_words]
            self.documents[doc_id] = ' '.join(without_stopWords)
            
        except ValueError:
            return "No article with given url exists"
        except Exception as e:
            return  'Unable to get document from URL '+str(e)      
             
    def remove_document(self, url):
        doc_id = url.split('wiki/',1)[1] 
        if doc_id in self.documents.keys():
            self.documents.pop(doc_id)
            return doc_id+" document successfully removed"
        return "There was no document inserted with the given url"   
     
    def search_document(self, keyword):
        results = []
        for doc_id, doc in self.documents.items():
            if keyword in doc:
                results.append(doc_id)
                print(self.documents[doc_id])
        if results==[]:
            print("No inserted document has the keyword \'"+keyword+"\'")   
  
    def search2(self, phrase):
        count = 0
        for doc in self.documents.values():
            if phrase in doc:
                count += 1
                continue
        return count
    
    def similar(self, doc_id1, doc_id2):
        try:
            doc1 = self.documents[doc_id1]
            doc2 = self.documents[doc_id2]
            # string doc to list (split) to set then intersect, common_words => set
            common_words = set(doc1.split()).intersection(set(doc2.split()))
            return len(common_words) / (len(doc1.split()) + len(doc2.split()))
        except KeyError:
            return ("invalid document id")
    
    def most_used_word(self, doc_id):
        if doc_id in self.documents.keys():
            doc = self.documents[doc_id]
            words = doc.split()
            word_count = {}
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                    
            avg=(sum(word_count.values())/len(word_count)) #sum(word_count.values())==len(words)
            most_used_words={ k:v for k,v in word_count.items() if v > avg }
            #most used word
            # most_used_word = None
            # most_used_word_count = 0
            # for word, count in word_count.items():
            #     if count > most_used_word_count:
            #         most_used_word = word
            #         most_used_word_count = count
            #  or
            # Max=max(word_count.values())
            # most_used_word= {x for x in word_count if word_count[x]==Max}
            # return  most_used_word
            return  list(most_used_words.keys())
        else:
            print(str(doc_id)+" is an invalid document id")
            
    def most_popular_word(self):
        all_words = []
        for doc_id, doc in self.documents.items():
            all_words.extend(doc.split())
        word_count = {}
        for word in all_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
                
        # same as  
        # most_popular_word = None
        # most_popular_word_count = 0
        # for word, count in word_count.items():
        #     if count > most_popular_word_count:
        #         most_popular_word = word
        #         most_popular_word_count = count
                
        if word_count.values(): 
            Max=max(word_count.values())
            most_popular_word= [x for x in word_count if word_count[x]==Max]       
            return most_popular_word    
    
#driver-test code 
sE=SearchEngine()
print(sE.add_document('https://en.wikipedia.org/wiki/Kytd'))
sE.add_document('https://en.wikipedia.org/wiki/Koala')
sE.add_document('https://en.wikipedia.org/wiki/Tiger')
sE.add_document('https://en.wikipedia.org/wiki/Computer')
# print(sE.documents)
print("inserted documents containing  the keyword \'animal\'=")
sE.search_document('animal')
print("inserted documents containing  the keyword \'species\'=")
sE.search_document('species')
print("inserted documents containing  the keyword \'word\'=")
sE.search_document('word')
print("how many document have the keyword \'animal\'=",sE.search2('animal'))
print("how many document have the keyword \'species\'=",sE.search2('species'))
print("similarity between \'Koala\'and \'Tiger\' document=",sE.similar('Koala','Tiger')) 
print("similarity between \'Koala\'and \'Tree\' document=",sE.similar('Koala','Tree')) 
print("most used word in \'Koala\' document'=",sE.most_used_word('Koala'))
print("most used word in \'tiger\' document=",sE.most_used_word('tiger'))
print("most popular word in all the documents=",sE.most_popular_word())
print(sE.remove_document('https://en.wikipedia.org/wiki/Data'))
print(sE.remove_document('https://en.wikipedia.org/wiki/Tiger'))
print(sE.documents) 


