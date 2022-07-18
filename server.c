//Server측

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#define PORT 51

void error_handling(char *message);

int main()
{
        int serv_sock;
        int clnt_sock;
        char buf[256];
        struct sockaddr_in serv_addr;
        struct sockaddr_in clnt_addr;
        socklen_t clnt_addr_size;
        char filename[1024];
        char message[]="Hello World!";


        serv_sock=socket(PF_INET, SOCK_STREAM, 0);
        if(serv_sock == -1)
                error_handling("socket() error");

        serv_addr.sin_family=AF_INET;
        serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);
        serv_addr.sin_port=htons(PORT);

        if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr))==-1 )          //ip와 port를 합쳐줌
                error_handling("bind() error");

        if(listen(serv_sock, 5)==-1)                    //접속하려는 클라이언트의 대기수
                error_handling("listen() error");

        while(1){            
            memset(&serv_addr, 0, sizeof(serv_addr));
            clnt_addr_size=sizeof(clnt_addr);
            clnt_sock=accept(serv_sock, (struct sockaddr*)&clnt_addr,&clnt_addr_size);      //Accept :연결수락, Connet : 서버소켓과 클라이언트 소켓의 연결을 시도
            if(clnt_sock==-1)
                    error_handling("accept() error");

            write(clnt_sock, message, sizeof(message));
            int nbyte = 256;
            size_t filesize = 0, bufsize = 0;
            FILE *file = NULL;

            recv(clnt_sock, filename, 1024, 0);

            file = fopen(filename/* 새로 만들 파일 이름 */, "wb");		//파일 이름 받기

            bufsize = 256;

            while(nbyte!=0) {
                nbyte = recv(clnt_sock, buf, bufsize, 0);
                fwrite(buf, sizeof(char), nbyte, file);
            }

            fclose(file);
            close(clnt_sock);
        }
        close(serv_sock);
        return 0;
}

void error_handling(char *message)
{
        fputs(message, stderr);
        fputc('\n', stderr);
        exit(1);
}
                            