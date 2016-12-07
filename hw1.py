


import datetime
import mediacloud, datetime

print "This file will display how many times Donald Trump and Hillary Clinton were mentioned in mainstream media during the month of September 2016"

mc = mediacloud.api.MediaCloud('media_cloud_api')


trumpMC = mc.sentenceCount('trump', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
clintonMC = mc.sentenceCount('clinton', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])

trumpCount = clintonCount = 0

trumpCount = trumpMC['count']
clintonCount = clintonMC['count']

print "Trump: %d" % trumpCount # prints the number of sentences found
print "Clinton: %d" % clintonCount # prints the number of sentences found
