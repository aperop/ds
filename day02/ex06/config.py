num_of_steps = 12
name_of_file = 'report'
type_of_file = 'txt'
template = '''
We have made {0} observations from tossing a coin: 
{1} of them were tails and {2} of them were heads. 
The probabilities are {3:.2f}% and {4:.2f}%, respectively. 
Our forecast is that in the text {5} observations we will have: 
{6} tail and {7} heads.
'''

log_file = 'analitics.log'
logging_format = "%(asctime)s %(message)s"

success = "The report has been successfully created"
error = "The report hasn't been created due to an error"
webhook_url = "https://hooks.slack.com/services/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"
