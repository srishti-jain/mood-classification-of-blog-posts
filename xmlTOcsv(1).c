#include<stdio.h>
#include<string.h>

int main(void)
{
	FILE *fin, *fout;
	fin = fopen("lj-amsterdam-moods.xml","r");
	fout = fopen("blogs.csv","w");
	
	long int totalBlogs = 0;
	
	char c = getc(fin);
	while(c != EOF)
	{
		if(c == '<')
		{
			char str[20];
			fscanf(fin,"%[^>]s",str);
			
			if(!strcmp(str,"item"))
			{
				totalBlogs++;
				c = getc(fin);//>
				while(1)
				{
					c = getc(fin);//next character	
					if(c == '<')
					{
						fscanf(fin,"%[^>]s",str);
						
						if(!strcmp(str,"/item"))
						{
							fputc('\n',fout);
if(totalBlogs == 309624) continue;
							//if(totalBlogs%100000 == 0)
								printf("Total number of blogs scanned:%ld\n",totalBlogs);
							break;
						}
						else if(!strcmp(str,"description"))
						{
							c = getc(fin);//>
							c = getc(fin);//next character
							while(c != '<')
							{
								if(c == '&')
								{
									c = getc(fin);
									if(c == 'l')
									{
										while(1)
										{
											c = getc(fin);
											if(c == '&')
											{
												c = getc(fin);
												if(c == 'g')
												{
													c = getc(fin);//t
													c = getc(fin);//;
													break;
												}
											}
										}
									}
									else if(c == 'q')
									{
										c = getc(fin);//u
										c = getc(fin);//o
										c = getc(fin);//t
										c = getc(fin);//;
										fputc('"',fout);
									}
									else if(c == 'a')
									{
										c = getc(fin);//p or m
										if(c == 'p')
										{
											c = getc(fin);//o
											c = getc(fin);//s
											c = getc(fin);//;
											fputc('\'',fout);
										}
										else if( c == 'm')
										{
											c = getc(fin);//p
											c = getc(fin);//;
											fputc('&',fout);
										}
									}
								}
								else
								{
									if(c != ',')
										fputc(c,fout);
								}
								c = getc(fin);
							}
							fscanf(fin,"%[^>]s",str);
							c = getc(fin);//>
						}
						else if(!strcmp(str,"lj:mood"))
						{
							c = getc(fin);//>
							fscanf(fin,"%[^<]s",str);
							fputc(',',fout);
							fputs(str,fout);
							c = getc(fin);//<
							fscanf(fin,"%[^>]s",str);
							c = getc(fin);//>
						}
									
						
					}
				}
			}
		}
		c = getc(fin);
	}
	
	printf("Total number of blogs scanned:%ld\n",totalBlogs);
	fclose(fin);
	fclose(fout);
	return 0;
}
