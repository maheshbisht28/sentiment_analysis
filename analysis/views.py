
from django.shortcuts import render
from .forms import MyForm ,MyForms, Myhash
from django.conf import settings
import pickle, os
import joblib
import tweepy
from sklearn.ensemble import AdaBoostClassifier
import pickle  

module_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT  = os.path.join(module_dir, 'media')
import re 
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
from django.http import HttpResponse
import json
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

def hasshh(request):
	if request.method == "POST":
		form=Myhash(request.POST)
		print("innnnnnnnnnnnnnnn")
		print(request.POST)
		print(form)
		if form.is_valid():
			print(form)
			result={}
			data=form.data['h']
		auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		from tweepy.models import Status
		api=tweepy.API(auth)
		cursor=tweepy.Cursor(api.search, q=data, tweet_mode="extended")
		import json
		count=0
		tweet=[]
		pre_tweet=[]
		print("----------------------------------------------------------------")
		for obj in cursor.items(14):
			print("ob ",obj)
			print("hereeeeee ",(obj.full_text.encode('ascii', errors='ignore')))
			tet=(obj.full_text.encode('ascii', errors='ignore')).decode('utf-8',"ignore")
			tweet.append(tet)
			pre_tweet.append(preprocess(tet))
			print(count)

			# print(preprocess(tet))
			# print(count)
			# if count==9:
			# 	break
			count=count+1

		file= os.path.join(settings.BASE_DIR, 'countvect_new_model.pkl')

		with open(file, 'rb') as file:
				test_cv = joblib.load(file)
				# test_cv=test_cv.transform(pre_tweet)
				# print("bisht ",test_cv)		
		test_count=[]
		for i in  pre_tweet:
			# print(i)
			test_count.append(test_cv.transform(i))
			# print("mahesh")
			# print(test_cv.transform(i))	
		file= os.path.join(settings.BASE_DIR, 'ada_boost_new_trained.pkl')

		with open(file, 'rb') as file:
			test = pickle.load(file)

		predict_reullt=[]
		for i in  test_count:
			# print(i)
			predict_reullt.append(test.predict(i))
		# return render(request,'test_new.html',{'form':form,'form1':form1,'hashtag':hashtag,'mylist':mylist})	
		# result['success']=test.predict(test_cv)
		data_new={}
		mylist = zip(tweet, predict_reullt )
		for i , d in mylist:
			data_new[i]=list(d)
			# print("i",i)
			# print("d",list(d))
		# print(type(data_new))	

		

		# print(pre)

		return HttpResponse(json.dumps(data_new),content_type = 'application/javascript; charset=utf8')



def test_sent(request):
	form = MyForm()
	form1 = MyForms()
	hashtag=Myhash()
	# print(form1)

	# print(hashtag)
	# for i,g in  mylist:
	# 	print(i)
	# 	print(g)	
	return render(request,'test_new.html',{'form':form,'form1':form1,'hashtag':hashtag})
		# 'tweet':tweet,'predict_reullt':predict_reullt})

def preprocess(data):
    corpus_temp=[]
    # for  i in range(0,len(data)):
    review=re.sub('[^a-zA-Z]',' ',data)

    review=re.sub('<.*?>',' ',review)
      # print(data['review'][i]);
      # print(data['sentiment'][i]);
    # print(i)
      
      

    # review=re.sub('[-+.^:,]',' ',review)

    # review = re.sub('[0-9]+',' ', review)

    # review=re.sub('[^a-zA-z0-9\s+]',' ',review)
    # review=re.sub('br','',review)
      
    # review=re.sub('https?://\S+|www\.\S+',' ',review)
    # review=re.sub("[,@\'?\.$*./#@&^@[]{}_`#$%^&*()+=?_~%]", "", review, flags=re.I)
    # review=re.sub("[\(\[].*?[\)\]]", "", review)
    # review=re.sub("_", "", review)
    # review=re.sub("`", "", review)
    # review = re.sub(' +', ' ',review)
    # review=[ps.stem(word) for word in review  if not word in  stopwords.words('english')]
    review=review.lower()
    review=review.split()
    temp=[]
    for word in review:
    	# print("ERs")
    	# print(review)
    	# print(word == 'not')
    	if word == 'not':
    		temp.append(ps.stem(word))

    	elif word not in stopwords.words('english'):
    		temp.append(ps.stem(word))
    review=temp			
    review=' '.join(review)
    corpus_temp.append(review)
    return corpus_temp 
def home(request):
	# consumer_key="HIj1xwzhVo37G0nfty3ziIaZB"
	# consumer_secret="41JDWYtXggEnOzmpU1DxbVSCdCMbN4Wq2tkBMmnUpJN1lizAbA"
	# access_token="1356999442168074241-clJ19NaunCtzFW7oGEgf59PJuG6qVf"
	# access_token_secret="4wGvZ36TBAlbOZU23dQ70DMgTs2nsXDVuPtwb7FgBMGtK"
	# # auth=tweepy.OAuthHandler(consumer_key)
	# # auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

	# auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
	# auth.set_access_token(access_token, access_token_secret)
	
	# from tweepy.models import Status
	
	# api=tweepy.API(auth)


	# # for obj in api.user_timeline(tweet_mode="extended"):
	# # 	print(obj.full_text.encode('ascii', errors='ignore'))

	# cursor=tweepy.Cursor(api.search, q='#WHUARS', tweet_mode="extended")
	
	# import json
	# count=0
	# tweet=[]


	# for obj in cursor.items():
	# 	print(obj.full_text.encode('ascii', errors='ignore'))
	# 	tweet.append(obj.full_text.encode('ascii', errors='ignore'))
	# 	if count==10:
	# 		break
	# 	count=count+1
	# print("mahesh")
	# print(tweet)		



	# str="very bad product %##"
	# pre=preprocess(str)
	# print("pre ",pre)

	
	# file= os.path.join(settings.BASE_DIR, 'counter_model.sav')

	# with open(file, 'rb') as file:
	# 	test_cv = joblib.load(file)
	# 	test_cv=test_cv.transform(pre)

	

	# file= os.path.join(settings.BASE_DIR, 'lda_model.pkl')

	# with open(file, 'rb') as file:
	# 	test = pickle.load(file)

	# test_lda=test.transform(test_cv)

	# file= os.path.join(settings.BASE_DIR, 'ala_analyzed_model.pkl')

	# with open(file, 'rb') as file:
	# 	test = pickle.load(file)

	# print("test ",test.predict(test_lda))

	return render(request,'home.html')
def sentiment(request):
	return render(request,'sentiment_import.html')
# Create your views here.
def type(request):
	form = MyForm()
	return render(request,'sentiment_type.html',{'form':form})

def types(request):
	form = MyForms()
	return render(request,'sentiment_types.html',{'form':form})
def test(request):
	# form = MyForm()
	return render(request,'index.html')
def sentiment_result(request):
	print("bisht")
	print(request.method == "POST" and request.is_ajax())
	if request.method == "POST":
		# print("maheshs")
		form=MyForm(request.POST)
		print("hereeeeeeeeeeeeee")
		print(request.POST)
		print(form.is_valid())
		print(form)
		if form.is_valid():
			print(form)
			result={}
			
			# print(form.data['a'])
			data=form.data['a']
			pre=preprocess(data)
			print("mahesh ",pre)
			# print("pre ",pre)

			file= os.path.join(settings.BASE_DIR, 'countvect_new_model.pkl')

			with open(file, 'rb') as file:
				test_cv = joblib.load(file)
				test_cv=test_cv.transform(pre)
				print("bisht ",test_cv)

			

			# file= os.path.join(settings.BASE_DIR, 'lda_model.pkl')

			# with open(file, 'rb') as file:
			# 	test = pickle.load(file)

			# test_lda=test.transform(test_cv)

			file= os.path.join(settings.BASE_DIR, 'ada_boost_new_trained.pkl')

			with open(file, 'rb') as file:
				test = pickle.load(file)

			# print("test ",type(test.predict(test_lda)))
			maahesh= test.predict(test_cv)
			print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
			# print(type(maahesh))
			print("test maahesh",test.predict(test_cv))
			result['success']=test.predict(test_cv)[0]
			print("result ",result)
			return HttpResponse(json.dumps(result),content_type="application/json")
	return render(request,'sentiment_result.html',{'result':test.predict(test_lda),
		                                            'data':data})	



def preprocess_list_of_sent(data):
	corpus_temp=[]
	for  i in range(0,len(data)):
		review=re.sub('[^a-zA-Z]',' ',data[i])
		review=review.lower()
		review=review.split()
		review=[ps.stem(word) for word in review  if not word in  stopwords.words('english')]
		review=' '.join(review)
		corpus_temp.append([review])
	return corpus_temp

def sentiment_results(request):
	print(request.POST)
	print("Cdccccccccccccccccddcccccccccc")
	if request.method == "POST":
		form=MyForms(request.POST)

	# 	print("maheshs")
		if form.is_valid():
	# 		print(form.data['a'])
	# 		data=form.data['a']
	# 		print("inside")
			text_ls=[]
			qr=request.POST
			print("mahesh ",qr)
			for i in qr.values():
				text_ls.append(i)
				print(i)
			text_ls.pop(10)
			print("text ",text_ls)	
			pre=preprocess_list_of_sent(text_ls)
			print("pre ",pre)
			result = []
			for i in pre:
				result.append(list(i))
			print(result)	

			predict_reullt=[]

			for i in pre:
				print(i)


				file= os.path.join(settings.BASE_DIR, 'countvect_new_model.pkl')

				with open(file, 'rb') as file:
					test_cv = joblib.load(file)
					test_cv=test_cv.transform(i)

				

				# file= os.path.join(settings.BASE_DIR, 'lda_model.pkl')

				# with open(file, 'rb') as file:
				# 	test = pickle.load(file)

				# test_lda=test.transform(test_cv)

				file= os.path.join(settings.BASE_DIR, 'ada_boost_new_trained.pkl')

				with open(file, 'rb') as file:
					test = pickle.load(file)


				print("test ",test.predict(test_cv))
				pre_t=test.predict(test_cv)
				predict_reullt.append(pre_t[0])
			print(predict_reullt)
			data={}

			# for i in range(len(predict_reullt)):
			# 	data["success "+i]=predict_reullt[i]
			# print(data)	





			return HttpResponse(json.dumps(predict_reullt),content_type="application/json")
	# 		post_count=0
	# 		neg_count=0
	# 		neut_count=0

	# 		for i in predict_reullt:
	# 			if i == 'negative':
	# 				neg_count+=1
	# 			elif i == 'positive':
	# 				post_count+=1
	# 			else:
	# 				neut_count+=1
	# 		print(post_count," ",neg_count," ",neut_count)
	# 		print(post_count+neg_count+neut_count)
	# 		post=(post_count*100)/(post_count+neg_count+neut_count)
	# 		neg=(neg_count*100)/(post_count+neg_count+neut_count)
	# 		neut=(neut_count*100)/(post_count+neg_count+neut_count)
	# 		print(post)
	# 		context={'post':post,'neg':neg,'neut':neut,}
	# 		return render(request,'sentiment_results.html',context)		



	return render(request,'sentiment_results.html')
		# {'result':test.predict(test_lda),
		#                                             'data':data})	
