Stream<int> timedCounter(Duration interval,[int? maxCount]) async*{
    int i =0;
    while(true){
        await Future.delayed(interval);
        yield i++;
        if (i == maxCount) break;
    }
}

void main(){
    final myStream = timedCounter(Duration(seconds:1));
    final subscription = myStream.listen(
       (data) => print('Data: $data') 
        );
    
}