import pandas as pd
import numpy as np

def main():
    
    filename='wiresharkop5.csv'     #add your file path to be read here

    df= pd.read_csv(filename)       #reading as pandas dataframe
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')       #replacing spaces with _ and formating to lower case

    port_no=np.unique(df[['source_port','destination_port']])       #fing all unique ports
    index=np.where(port_no<=49152) #for dynamic or private ports
    port_no=np.delete(port_no,index)   #removing the found port numbers

    f = open('HW2_2_output.txt', 'a')       #opening text file to write the output
    f.write('Total number of TCP connections: {0}\n'.format(len(port_no)))  
    print('Total number of TCP connections: ',len(port_no))

    #rows of dataframe
    f.write('Total number of packets in the trace: {0}\n'.format(df.shape[0]+1))
    print('Total number of packets in the trace: ',df.shape[0]+1)

    f.write('Total amount of traffic (packet sizes) in the trace: {0} \n'.format(df.length.sum()))
    print('Total amount of traffic (packet sizes) in the trace: ',df.length.sum())

    #dictonary to store the data for each TCP connection
    dict_op={ 'No':[],'Source IP':[],'Destination IP':[],'TCP port 1':[],'TCP port 2':[],'No pkts src to dst':[],'No pkts dst to src':[],'Traffic src to dst':[],
            'Traffic dst to src':[],'RT considering SYN':[],'RT considering first available packet in trace':[] } 

    count=1
    # for each TCP connection i.e for each unique port number found
    for i in port_no:
        pck_sd=(df.loc[df['source_port'] == i])          #packet data flowing from src to dst
        pck_ds=(df.loc[df['destination_port'] == i])     #packet data flowing from dst to src
        try:     
            temp=(pck_sd['info'].values[0]).split()     #checking if packet contains SYN packet
            
            #temp2 considers the Response time from first SYN packet if there is no SYN packet found it says "No SYN packet found"
            #temp3 calculates response time just between first packet found in trace to its last packet
            if (temp[3] == '[SYN]' ):
                temp2= round((pck_ds['time'].iloc[-1])-(pck_sd['time'].values[0]),4)
                temp3=temp2
            else:
                temp2="No SYN packet found"
                temp3= round((pck_ds['time'].iloc[-1])-(pck_sd['time'].values[0]),4)
            
            dict_op['No'].append(count)
            dict_op['Source IP'].append( pck_sd['source'].values[0] )
            dict_op['Destination IP'].append( pck_sd['destination'].values[0] )
            dict_op['TCP port 1'].append( pck_sd['source_port'].values[0] )
            dict_op['TCP port 2'].append( pck_sd['destination_port'].values[0] )
            dict_op['No pkts src to dst'].append( pck_sd['no.'].count() )
            dict_op['No pkts dst to src'].append( pck_ds['no.'].count() )
            dict_op['Traffic src to dst'].append( pck_sd.length.sum() )
            dict_op['Traffic dst to src'].append( pck_ds.length.sum() )
            dict_op['RT considering SYN'].append( temp2 )
            dict_op['RT considering first available packet in trace'].append( temp3 )

            count+=1

        #if there are no packets captured in trace form src to dst
        except(IndexError):
            #when there are packet captured from dst to src
            if (pck_sd.empty and not pck_ds.empty):
                dict_op['No'].append(count)
                dict_op['Source IP'].append( pck_ds['destination'].values[0] )
                dict_op['Destination IP'].append( pck_ds['source'].values[0] )
                dict_op['TCP port 1'].append( pck_ds['destination_port'].values[0] )
                dict_op['TCP port 2'].append( pck_ds['source_port'].values[0] )
                dict_op['No pkts src to dst'].append( pck_sd['no.'].count() )
                dict_op['No pkts dst to src'].append( pck_ds['no.'].count() )
                dict_op['Traffic src to dst'].append( pck_sd.length.sum() )
                dict_op['Traffic dst to src'].append( pck_ds.length.sum() )
                dict_op['RT considering SYN'].append( temp2 )
                dict_op['RT considering first available packet in trace'].append( temp3 )

                count+=1
            if pck_ds.empty and pck_sd.empty:
                continue

    df2 = pd.DataFrame.from_dict(dict_op)   #creating pandas dataframe from the data stored in the list

    df2.to_csv(f, sep='\t', index=False)    #writing to the output file 
    print(df2)  
    f.close()

if __name__=="__main__":
    main()