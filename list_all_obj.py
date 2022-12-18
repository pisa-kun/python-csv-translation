import boto3
s3 = boto3.resource('s3')
def get_all_objects_high(bucket):
    bucket = s3.Bucket(bucket)
    return bucket.objects.all()

for bucket in s3.buckets.all():
    objs = get_all_objects_high(bucket.name)
    for i,obj in enumerate(iter(objs)):
        print(f'{bucket.name} {i}: {obj.key}')