/* server.c */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define POST 51     //Django Server Port

void error_handling(char *message);

int main()            //Client측 Port를 입력받음-추후 수정(Port 고정하여 실행파일만 실행하는 방식으로)
{
	int serv_sock;
	int clnt_sock;
	char buf[256];
	struct sockaddr_in serv_addr;
	struct sockaddr_in clnt_addr;
	socklen_t clnt_addr_size;

	char message[]="Send Security Mgnt";
	
	serv_sock=socket(PF_INET, SOCK_STREAM, 0);
	if(serv_sock == -1)
		error_handling("socket() error");
			
	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family=AF_INET;
	serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);
	serv_addr.sin_port=htons(PORT);                        //Client측 Port(argv[1])
	
	if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr))==-1 )
		error_handling("bind() error"); 
	
	if(listen(serv_sock, 5)==-1)
		error_handling("listen() error");
	
	clnt_addr_size=sizeof(clnt_addr);  
	clnt_sock=accept(serv_sock, (struct sockaddr*)&clnt_addr,&clnt_addr_size);
	if(clnt_sock==-1)
		error_handling("accept() error");  
	
	write(clnt_sock, message, sizeof(message));
	int nbyte = 256;
    size_t filesize = 0, bufsize = 0;
    FILE *file = NULL;

    file = fopen("aurora.jpg"/* 새로 만들 파일 이름 */, "wb");      //파일이름 Client측 파일이름으로 수정해야함

    //ntohl(filesize);
	//recv filesize

	//recv(clnt_sock, &filesize, sizeof(filesize), 0);
    //ntohl(filesize);
	//printf("file size = [%ld]\n", filesize);
    bufsize = 256;

    while(/*filesize != 0*/nbyte!=0) {
 		//if(filesize < 256) bufsize = filesize;
        nbyte = recv(clnt_sock, buf, bufsize, 0);
		//printf("filesize:%ld nbyte: %d\n", filesize, nbyte);

 		//filesize = filesize -nbyte;

        fwrite(buf, sizeof(char), nbyte, file);		
        //nbyte = 0;
    }
 
/*
	while((nbyte = recv(clnt_sock, buf, bufsize, 0) != 0)){
 		fwrite(buf, sizeof(char), nbyte, file);
	}
*/	

	fclose(file);
	close(clnt_sock);	
	close(serv_sock);
	return 0;
}

void error_handling(char *message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}