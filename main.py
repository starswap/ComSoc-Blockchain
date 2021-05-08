from flask import Flask, render_template, request
import time
from blockchain import Block, Blockchain

web_site = Flask(__name__)


@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/chainGraphic') #Add arrow image between?
def chainGraphic():
	return render_template('showChain.html',enumChain=enumerate(JamesCoin.chain))

@web_site.route('/user/', defaults={'username': None})
@web_site.route('/user/<username>')
def generate_user(username):
	if not username:
		username = request.args.get('username')

	if not username:
		return 'Sorry error something, malformed request.'

	return render_template('personal_user.html', user=username)


start = time.time()
JamesCoin = Blockchain(Block("James is the genesis"),3)
JamesCoin.mineBlock(Block("Santosh is the most intriguing geographer",JamesCoin.chain[0].getHash())) #Should Deal with this for you when creating
end = time.time()
print("Total time in seconds : " + str(end-start))
web_site.run(host='0.0.0.0', port=8080)