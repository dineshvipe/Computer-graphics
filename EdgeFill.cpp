#include <GL/glut.h>
#include <math.h>
#include <stdio.h>


int pix[480][640];

void fillpix(){
int k,l;
    for(k=0;k<480;k++){
        for(l=0;l<640;l++){
        pix[k][l]=0;
        }
    }

}

void edgefill(double x1,double y1,double x2,double y2){
    double i,m;
    int j;
    m=(y2-y1)/(x2-x1);
    
    if(x2==x1){
        for(j=y1;j<y2;j++){
            for(i=x1;i<640;i++){
                if(i+0.5>x1){
                    int u=floor(i);
                    
                    if(pix[j][u]==0){
                        glColor3f(1.0,0.0,1.5);
                        glVertex2d(u,j);
                        pix[j][u]=1;
                    }

                    else{
                        glColor3f(1.0,1.0,1.5);
                        glVertex2d(u,j);
                        pix[j][u]=0;
                    
                    }
                
                }
            }
        }
    }

    else if(m!=0){
        double xa,temp;
        if(x1<x2)
            temp=x1;
        else
            temp=x2;

        for(j=y1;j<y2;j++){
    
            xa=(j-y2+m*x2)/m;
            for(i=xa;i<640;i++){
        
                if(i+0.5>temp){
                    int u=floor(i);
            
                    if(pix[j][u]==0){
                        glColor3f(1.0,0.0,1.5);
                
                        glVertex2d(u,j);
                        pix[j][u]=1;
                    }

                    else{
                        glColor3f(1.0,1.0,1.5);
                        glVertex2d(u,j);
                        pix[j][u]=0;
                
                    }
        
                }
        
            }   
    
        }
    
    }
}


int sign(int a){

    if(a>0)
        return 1;
    if(a<0)
        return -1;
    else
        return 0;


}

void bress(double x1,double y1,double x2,double y2){

    double x,y,dx,dy;
    double m;
    int s1,s2,ch=0;
    int e;
  

    x=x1;
    y=y1;

    dx=abs(x2-x1);
    dy=abs(y2-y1);
  
    s1=sign(x2-x1);
    s2=sign(y2-y1);
  

    int temp;
  
    if(dy>dx){
        temp=dx;
        dx=dy;
        dy=temp;
        ch=1;
        }
        else
        {
        ch=0;
        }


    e=((2*dy)-dx);
    int i;
  
    for(i=0;i<dx;i++){
    glVertex2d(floor(x),floor(y));

    while(e>0){
  
        if(ch==1){
        x=x+s1;
        }
        else{
        y=y+s2;
        }

    e=e-2*(dx);
    }

    if(ch==1)
        y=y+s2;
    else
        x=x+s1;

    e=(e+2*(dy));
  
  
  
    }
}

void Primitives(void){
    int ymin,ymax;
    ymin=30;
    ymax=210;
    
     glClear(GL_COLOR_BUFFER_BIT);

     glColor3f(1.0f,0.0f,0.0f);
     glBegin(GL_POINTS);
     glPointSize(2.0f);
     fillpix();

     bress(30,30,30,210);
     bress(30,30,240,30);
     bress(240,30,240,180);
     bress(240,180,150,90);
     bress(150,90,30,210);
    
    edgefill(30,30,30,210);
    edgefill(150,90,30,210);
    edgefill(240,30,240,180);
    edgefill(150,90,240,180);
    glEnd();
    glFlush();


}


void init(void){
    glClearColor(1.0,1.0,1.0,0.0);
    glColor3f(1.0,0.0,0.0);
    glViewport(0,0,640,480);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,640,0,480);
}

int main(int argc,char** argv){
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutInitWindowSize(640,480);
    glutInitWindowPosition(0,0);
  
    glutCreateWindow("Primitives");
    init();
    glutDisplayFunc(Primitives);
   
    glutMainLoop();
    return 0;
}