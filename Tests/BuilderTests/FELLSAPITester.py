import unittest
from requests import post, get
import json
import requests
from urllib import parse
from threading import Timer


class FELLSAPITester(unittest.TestCase):

    def test_check_job_status(self):
        test_job_id = "5acb64e20fe7e54308d3f853"
        base_url = "http://protein.bio.unipd.it/fellsws/status/"
        check_status = get(base_url+test_job_id)
        json_data = check_status.content.decode('utf-8')
        json_parsed = json.loads(json_data)
        status = json_parsed['status']
        self.assertEqual("done", status)
        check_status.close()


    # make a sequence object and translate to fasta
    # or make fasta strings for testing
    # check that the response is good (200) and make sure it contains a request ID

    def test_send_request(self):
        #
        request_url = "http://protein.bio.unipd.it/fellsws/submit"

        necessary_header = {'Content-Type': 'multipart/form-data; boundary=XXX'}
        request_body_begin = '--XXX\nContent-Disposition: form-data; name="sequence"' \
                             '\n\n>myseq\nMVHLTPEEKSAVTALWGKVNVDEVGG\n--XXX--'
        # parse out id
        url_body = parse.quote(request_body_begin)
        sent_request = requests.Request(headers=necessary_header, method='POST', url=request_url, data=url_body)
        s = requests.Session()
        prep = sent_request.prepare()
        print(prep.body)
        print(prep.path_url)
        response = s.send(prep)
        status = response.content
        print(status)
        s.close()
        # self.assertEqual(True, False)

    def test_prepare

    def test_export_data(self):
        self.assertEqual(True, True)


class SODAAPITester(unittest.TestCase):

    def test_return_request_status(self):
        request_url = "http://protein.bio.unipd.it/sodaws/submitsoda"

        # necessary_header = {'Content-Type': 'multipart/form-data; boundary=XXX'}
        request_body = {'sequence': 'MVHLTPEEKSAVTALWGKVNVDEVGG'}

        sent_request = requests.Request(method='POST', url=request_url, data=request_body)
        prep = sent_request.prepare()
        # print(prep.headers)
        # print(prep.body)
        session = requests.Session()
        response = session.send(prep)
        json_response = response.json()
        response_json = json_response['jobid']
        print(response_json)
        print(response.content)
        # path = "/Users/coltongarelli/Desktop/"
        # add = "newFile"
        # full = os.path.join(path, add)
        url = "http://protein.bio.unipd.it/sodaws/status/"
        self.get_update(url+response_json)
        session.close()

    def get_update(self, url):
        data = get(url)
        json_parsed = json.loads(data.content.decode('utf-8'))
        status = json_parsed['status']
        self.timer(status, url)
        return True



    # def test_return_result(self):
    #     url = "http://protein.bio.unipd.it/sodaws/result/5acd38a6496e7ce82285d235"
    #     results = get(url)
    #     json_format = {"_id":"5acd38a6496e7ce82285d235","chain":"null","disorder_array":["0.352194","0.358856","0.342157","0.246562","0.190068","0.143201","0.106856","0.0915666","0.0769444","0.0678653","0.058806","0.0495826","0.0447009","0.0421334","0.0363421","0.0305723","0.0251401","0.0202754","0.0162846","0.0137588","0.0120604","0.0111304","0.0105612","0.0103016","0.00978176","0.00954417","0.00983271","0.00953143","0.00956413","0.00955347","0.00944656","0.00876906","0.00882009","0.00902242","0.010108","0.0117172","0.0143472","0.0174323","0.0230465","0.0313814","0.0472863","0.0733263","0.107925","0.15315","0.232436","0.248276","0.225656"],"energy_array":["-1.88282","-2.376304","-2.771739","-2.925191","-3.444724","-3.964384","-5.231135","-5.845792","-6.260945","-6.33091","-6.836628","-7.030792","-7.127364","-7.376408","-7.679964","-8.394324","-8.838157","-9.26566","-9.539247","-9.62728","-9.728754","-9.762317","-9.80582","-9.820015","-9.838581","-9.845104","-9.852679","-9.855337","-9.858212","-9.859135","-9.859055","-9.857807","-9.856723","-9.853061","-9.843688","-9.834639","-9.811319","-9.790968","-9.734632","-9.686341","-9.640386","-9.527828","-9.414219","-9.041367","-8.916057","-8.45419","-7.459683"],"helix_array":["0.00351623","0.0542996","0.0920631","0.0755255","0.542262","0.768013","0.875482","0.922549","0.949523","0.948158","0.933494","0.907691","0.835251","0.715648","0.623814","0.644519","0.665374","0.714549","0.712057","0.747651","0.777343","0.783873","0.806223","0.819037","0.825893","0.852211","0.889152","0.908054","0.92025","0.931707","0.934596","0.935272","0.926596","0.911504","0.884019","0.853248","0.831413","0.82252","0.78377","0.748695","0.664744","0.584234","0.492245","0.411297","0.324977","0.157716","0.00322963"],"mask":"11111111111111111111111111111111111111111111111","mod":"sequence","pdbname":"null","sequence":"ASFDSDQWWEQWASDASQWQWQWQWQWQWWWQWWQWQWQQWQWDFSD","soda_output":"-1.88282,-2.376304,-2.771739,-2.925191,-3.444724,-3.964384,-5.231135,-5.845792,-6.260945,-6.33091,-6.836628,-7.030792,-7.127364,-7.376408,-7.679964,-8.394324,-8.838157,-9.26566,-9.539247,-9.62728,-9.728754,-9.762317,-9.80582,-9.820015,-9.838581,-9.845104,-9.852679,-9.855337,-9.858212,-9.859135,-9.859055,-9.857807,-9.856723,-9.853061,-9.843688,-9.834639,-9.811319,-9.790968,-9.734632,-9.686341,-9.640386,-9.527828,-9.414219,-9.041367,-8.916057,-8.45419,-7.459683\n0.352194,0.358856,0.342157,0.246562,0.190068,0.143201,0.106856,0.0915666,0.0769444,0.0678653,0.058806,0.0495826,0.0447009,0.0421334,0.0363421,0.0305723,0.0251401,0.0202754,0.0162846,0.0137588,0.0120604,0.0111304,0.0105612,0.0103016,0.00978176,0.00954417,0.00983271,0.00953143,0.00956413,0.00955347,0.00944656,0.00876906,0.00882009,0.00902242,0.010108,0.0117172,0.0143472,0.0174323,0.0230465,0.0313814,0.0472863,0.0733263,0.107925,0.15315,0.232436,0.248276,0.225656\n0.00351623,0.0542996,0.0920631,0.0755255,0.542262,0.768013,0.875482,0.922549,0.949523,0.948158,0.933494,0.907691,0.835251,0.715648,0.623814,0.644519,0.665374,0.714549,0.712057,0.747651,0.777343,0.783873,0.806223,0.819037,0.825893,0.852211,0.889152,0.908054,0.92025,0.931707,0.934596,0.935272,0.926596,0.911504,0.884019,0.853248,0.831413,0.82252,0.78377,0.748695,0.664744,0.584234,0.492245,0.411297,0.324977,0.157716,0.00322963\n0.00178014,0.0420264,0.0616931,0.0220985,0.00625187,0.00588062,0.0111769,0.0155178,0.0172821,0.0200841,0.0189168,0.018429,0.0154555,0.0124632,0.0101724,0.00979777,0.0146306,0.0311015,0.0503906,0.0591464,0.0670203,0.0672214,0.0644789,0.0578354,0.052529,0.0420002,0.0390381,0.0379422,0.0375786,0.0338247,0.0323974,0.0287591,0.027869,0.0288437,0.030648,0.0329438,0.0353229,0.0373626,0.0426614,0.0549183,0.0737699,0.102102,0.121934,0.111608,0.0662262,0.0299637,0.00148578\n-89.34716699,37.7647804,-144.4751307,170.9113805,12.37707774,135.70114224,129.1063128,-3.8365242,-5.599119,124.3852468,124.5776116,-4.3716278,-135.9343502,-0.3339668,138.846179,-127.89501486,0.6380584,132.8241928,2.7033104,130.8836314,-0.6603996,128.9846096,-2.1606668,127.183446,-3.18271648,125.49964574,-6.32338538,122.74496426,-7.85617654,-8.42602166,-8.57057108,121.38892132,-8.18654882,-7.44102476,123.920893,-4.554469,126.5487842,-2.9848582,128.9920538,130.8002034,5.0292704,139.1955626,13.925494,148.334596,-162.2426056,26.3742054,169.83634869\n\n","solubility_array":["-89.34716699","37.7647804","-144.4751307","170.9113805","12.37707774","135.70114224","129.1063128","-3.8365242","-5.599119","124.3852468","124.5776116","-4.3716278","-135.9343502","-0.3339668","138.846179","-127.89501486","0.6380584","132.8241928","2.7033104","130.8836314","-0.6603996","128.9846096","-2.1606668","127.183446","-3.18271648","125.49964574","-6.32338538","122.74496426","-7.85617654","-8.42602166","-8.57057108","121.38892132","-8.18654882","-7.44102476","123.920893","-4.554469","126.5487842","-2.9848582","128.9920538","130.8002034","5.0292704","139.1955626","13.925494","148.334596","-162.2426056","26.3742054","169.83634869"],"status":"entryReady","strand_array":["0.00178014","0.0420264","0.0616931","0.0220985","0.00625187","0.00588062","0.0111769","0.0155178","0.0172821","0.0200841","0.0189168","0.018429","0.0154555","0.0124632","0.0101724","0.00979777","0.0146306","0.0311015","0.0503906","0.0591464","0.0670203","0.0672214","0.0644789","0.0578354","0.052529","0.0420002","0.0390381","0.0379422","0.0375786","0.0338247","0.0323974","0.0287591","0.027869","0.0288437","0.030648","0.0329438","0.0353229","0.0373626","0.0426614","0.0549183","0.0737699","0.102102","0.121934","0.111608","0.0662262","0.0299637","0.00148578"],"title":">test"}
    #     json_obj = json.dumps(json_format)
    #     print(results.content.decode('utf-8'))
    #     self.assertEqual(results.content.decode('utf-8'), json_obj)


if __name__ == '__main__':
    unittest.main()
