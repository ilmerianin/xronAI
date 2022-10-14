import speedtest

s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
s.results.share()

result_dict = s.results.dict()
print('результат теста:',result_dict())
