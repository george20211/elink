import geoip2.database

reader = geoip2.database.Reader('C:\dev\e-link\elink\elink\data.mmdb')

class DetectCountry():

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        try:
            obj = reader.country(ip)
        except:
            obj = 404
        return obj
