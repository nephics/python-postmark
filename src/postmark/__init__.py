__version__ = '0.1.4'
__author__  = "David Martorana (http://davemartorana.com)"
__date__    = '2010-January-01'
__url__     = 'http://postmarkapp.com'
__copyright__ = "(C) 2009-2010 David Martorana, Wildbit LLC, Python Software Foundation."

__doc__ = '''

    PMMail object for Postmark (http://postmarkapp.com)

    Version: ''' + __version__ + '''
    Author: ''' + __author__ + '''
    Date: ''' + __date__ + '''

    CHANGE LOG:
    
        Version 0.1.4
            - Added ".reply_to" property.  The "ReplyTo" custom header is unallowed by Postmark 
              now, and their documentation has been updated to reflect the change.
              http://developer.postmarkapp.com

        Version 0.1.3
            - Major fix to the way properties were being used, fixes doc strings in properties
            - "custom_headers" is now always a dict, even if set to None

        Version 0.1.2
            - Added 'custom_headers' property (must be a dictionary) to PMMail object
            - Added optional 'test' argument to send function to print JSON message instead of actually sending it
            
        Version 0.1.1:
            - Initial release

    USEAGE:
        Make sure you have a Postmark account.  Visit
        http://postmarkapp.com to sign up for an account.
        Requires a Postmark API key.
    
        Import postmark.PMMail to use Postmark.  Check
        class documentation on PMMail object for more 
        information.
        
    DJANGO:
        The library can be used stand-alone with Django.  You can also
        add the setting 
        
        POSTMARK_API_KEY = 'your-key'
        POSTMARK_SENDER = '<From Name> from@emailaddress.com'
        
        to your settings.py file, and when you create a new PMMail object,
        it will grab the API key automatically.
        

    EXCEPTIONS:
        PMMailMissingValueException(Exception):
            One of the required values for attempting a send request is missing

        PMMailSendException(Exception):
            Base Postmark send exception

        PMMailUnauthorizedException(PMMailSendException):
            401: Unathorized sending due to bad API key

        PMMailUnprocessableEntityException(PMMailSendException):
            422: Unprocessable Entity - usually an exception with either the sender
            not having a matching Sender Signature in Postmark.  Read the message
            details for further information
    
        PMMailServerErrorException(PMMailSendException):
            500: Internal error - this is on the Postmark server side.  Errors are
            logged and recorded at Postmark.

        PMMailURLException(PMMailSendException):
            A URLError was caught - usually has to do with connectivity
            and the ability to reach the server.  The inner_exception will
            have the base URLError object.
            
    TODO: 
        Add automatic multipart emails via regex stripping of HTML tags from html_body
        if the .multipart property is set to True

'''


from core import *