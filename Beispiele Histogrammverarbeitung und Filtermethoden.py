#!/usr/bin/env python
# coding: utf-8

# # Histogrammverarbeitung und Filtermethoden
# 
# Matlab-Code und Bilder zu den Beispielen in der Ausarbeitung zum Thema Histogrammverarbeitung und Filtermethoden
# 
# Die Folgenden Beispiele wurden in Matlab implementiert. Der Code ist (wenn nicht anders angegeben) von Karla Schöne geschrieben, mit der Hilfe der auf Matlab Community Seite Matlab Answers erklärten Funktionen und Beispiele.

# ## verwendetes Originalbild
# ![Lena_River_Delta.jpg](attachment:Lena_River_Delta.jpg)
# Quellen: Copernicus Sentinel data (2019), processed by ESA, CC BY-SA 3.0 IGO;
#          https://www.esa.int/ESA_Multimedia/Images/2019/06/Lena_River_Delta

# 
# 
# 
# 
# ## Histogrammverarbeitung
# ### Intensity Scaling
# matlab-code:
%Bild einlesen und in Graustufenbild umwandeln
picture = imread('Lena_River_Delta.jpg');
I = rgb2gray(picture);

%Bild über Funktion imadjust verarbeiten und Originalbild und verarbeitetes Bild geimeinsam ausgeben
J = imadjust(I);
imshowpair(I,J,'montage')
title('Originales Bild (links) Vs. Intensity Scaling (rechts)')

%die Histogramme beider Bilder nebeneinader ausgeben
figure
subplot(1,2,1)
imhist(I,64)
title('Originales Histogramm') 
subplot(1,2,2)
imhist(J,64)
title('Histogramm nach Intensity Scaling')
# Histogramme:
# ![Hist_IntSca.jpg](attachment:Hist_IntSca.jpg)
# Bilder: Originales Bild (links) Vs. Intensity Scaling (rechts)
# ![Pic_IntSca.jpg](attachment:Pic_IntSca.jpg)

# ### Histogram Equalization
# matlab-code:
%Bild einlesen und in Graustufenbild umwandeln
picture = imread('Lena_River_Delta.jpg');
I = rgb2gray(picture);

%Bild über Funktion histeq equalisieren
J = histeq(I);

%Bild mit dazugehörigem Histogramm ausgeben
figure
subplot(1,2,1); imshow(I); title('Originalbild')
subplot(1,2,2); imhist(I,64); title('Histogramm des Originalbildes')

%verbessertes Bild mit dazugehörigem Histogramm ausgeben
figure
subplot(1,2,1); imshow(J); title('verbessertes Bild');
subplot(1,2,2); imhist(J,64); title('Histogramm des verbesserten Bildes')

%Kummuliertes Histogramm über histeq ausgeben
[J,T] = histeq(I);
figure
plot((0:255)/255,T); title('kummuliertes Histogramm');
# Originalbild mit Histogramm:
# ![OrigPic_HistEqua.jpg](attachment:OrigPic_HistEqua.jpg)
# kummuliertes Histogramm:
# ![kummulierteshist.jpg](attachment:kummulierteshist.jpg)
# verbessertes Bild mit Histogramm:
# ![ImpPic_HistEqua.jpg](attachment:ImpPic_HistEqua.jpg)

# ### Histogrammspezifizierung
# matlab-code:
%Bild einlesen, in Graustufenbild umwandlen und Referenzbild einlesen
picture = imread('Lena_River_Delta.jpg');
img_gray = rgb2gray(picture);
ref = imread('Luis.png');

%Bild über Referenzbild verbessern
HistImRRef = imhist(ref)./numel(ref);
EnhPic = histeq(img_gray,HistImRRef);

%Originalbild, Referenzbild und verbessertes Bild ausgeben
figure;
subplot(223);imshow(ref);title('Referenzbild');
subplot(221);imshow(img_gray);title('Originalbild');
subplot(222);imshow(EnhPic);title('mit Histogram Specification verbessertes Bild');
# Originalbild, verbessertes Bild und Referenzbild:
# ![image.png](attachment:image.png)
# Quelle (Referenzbild): Hund Luis, fotografiert von C.P.Börner 

# ### Histogramm Statistik
# matlab-code:
Isem=imread('Lena_River_Delta.jpg');
grayImage = rgb2gray(Isem);
Iblur = imgaussfilt(grayImage,1);
%J = imnoise(grayImage,'salt & pepper',0.02);

f=double(Iblur);
M=mean2(f);D=std2(f);
M
D

Bsize=[3 3];
k=[0.4 0.02 0.4];
E=4.0;
tic
fsem_enh=nlfilter(f,Bsize,@mylocstat,M,D,E,k);
t_nlfilter = toc;
Isem_enh=im2uint8(mat2gray(fsem_enh));

subplot(1,2,1),imshow(Iblur),title('Originalbild')
subplot(1,2,2),imshow(Isem_enh),title('Verbessertes Bild mit Histogramm Statistik')
# Quelle: Alex Zuo (zuoxinian@yahoo.com.cn)

# Originalbild und verbessertes Bild:
# ![HistStats.jpg](attachment:HistStats.jpg)

# 
# ## Filtermethoden
# ### Gauss Filter
# matlab-code:
%Bild einlesen und in Graustufenbild umwandeln
I = imread('Lena_River_Delta.jpg');
grayImage = rgb2gray(I);
%Bild mit Gauss Filter bearbeiten
Iblur = imgaussfilt(grayImage,4);
%Originalbil und verbessertes Bild darstellen
figure
imshowpair(grayImage,Iblur,'montage'); 
title('Originales Bild (links) Vs. nach Gauss gefiltertes Bild (rechts); mit σ=4')
# Originalbild und verbessertes Bild:
# ![Gauss.jpg](attachment:Gauss.jpg)

# ### Medianfilter
# matlab-code:
%Bild einlesen und in Graustufenbild umwandeln
picture = imread('Lena_River_Delta.jpg');
grayImage = rgb2gray(picture);

%Bild convertieren, salt&pepper Noise drauflegen und mit Medianfilter filtern
ImgCon = im2uint8(grayImage)
SPImg = imnoise(ImgCon,'salt & pepper',0.02);
MedImg = medfilt2(SPImg, [3 3]);

%Salt&Pepper Bild und gefiltertes Bild darstellen
figure
imshowpair(SPImg,MedImg,'montage')
title('mit salt& pepper noise vs. mit Medianfilter bearbeitet')
# Bild mit Salt & Pepper noise und mit Medianfilter bearbeitet:
# ![MedFlt.jpg](attachment:MedFlt.jpg)

# ## Laplace-Filter
# matlab-code:
 %Bild einlesen und in Graustufenbild umwandeln
 picture=imread('Lena_River_Delta.jpg');
 grayImage = rgb2gray(picture);
 
 %Bild über Laplace Filter verbessern
 w=fspecial('laplacian',0); 
 EnhImg=imfilter(grayImage,w,'replicate');
 
 %Originalbild und verbessertes Bild darstellen
 figure,imshowpair(grayImage, EnhImg, 'montage');
 title('Originalbild vs. bearbeitetes Bild mit Laplace Filter')
# Originalbild und bearbeitetes Bild mit Laplace Filter:
# ![Laplace.jpg](attachment:Laplace.jpg)

# ## Unschärfe Masken
# matlab-code:
%Bild einlesen und in Graustufenbild umwandeln und unscharf machen (mit Gauss)
picture = imread('Lena_River_Delta.jpg');
grayImage = rgb2gray(picture);
blurgray = imgaussfilt(grayImage,3);

%Bild mit imsharpen Funktion bearbeiten
J=imsharpen(blurgray,'Radius',5,'Amount',2);

%Originalbild und verbessertes Bild darstellen
figure, imshowpair(blurgray,J,'montage')
title('Originalbild vs. Bild nach Anwendung von Unschärfemasken');
# Originalbild und Bild nach Anwendung von Unschärfemasken:
# ![unsharpmask.jpg](attachment:unsharpmask.jpg)

# ## Gradientenfilter
# matlab-code:
%Bild einlesen und in Graustufenbild umwandeln
picture = imread('Lena_River_Delta.jpg');
grayImage = rgb2gray(picture);

%Bild verbessern mit Funktion imgradient
enhgray = imgradient(grayImage);

%Originalbild und verbessertes Bild darstellen
figure, imshowpair(grayImage,enhgray,'montage')
title('Originalbild vs. Bild bearbeitet mit Gradientenmethode')
# Originalbild und Bild bearbeitet mit Gradientenmethode:
# ![GradMeth.jpg](attachment:GradMeth.jpg)
