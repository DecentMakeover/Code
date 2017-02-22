import movie
import fresh_tomatoes


shutter_island = movie.Movie('Shutter island',
                             'A patient being treated in an unconventaional way',
                             'http://2.bp.blogspot.com/_kqwU0XOOn0o/TR4qty1-4EI/AAAAAAAABto/dyRKolLidiI/s1600/Shutter-Island.jpg',
                             'https://www.youtube.com/watch?v=5iaYLCiq5RM')



print (shutter_island.storyline)

the_secret_in_thier_eyes = movie.Movie('The Secret in thier Eyes',
                                       'Lets not spoil it for you',
                                       'https://jssherald.files.wordpress.com/2013/07/secret-in-their-eyes-the-2009-poster.jpg',
                                       'https://www.youtube.com/watch?v=EFF8wXGF9Yw')
print(the_secret_in_thier_eyes.storyline)

#the_secret_in_thier_eyes.show_trailer()

life_of_david_gale = movie.Movie('Life of David Gale',
                                 'Proffesor accused of rape of a student and murder,is he innocent?',
                                 'http://68.media.tumblr.com/092be79194d072bd2f5d90c2442b1d3e/tumblr_nifnksjn0e1t0t91ao1_1280.jpg',
                                 'https://www.youtube.com/watch?v=gt7Jmjwjk3I')


#life_of_david_gale.show_trailer()

the_counsellor = movie.Movie('The Counsellor',
                             'What if you had everything,and still wanted more',
                             'https://bxerblog.files.wordpress.com/2014/08/the-counselor.jpg',
                             'https://www.youtube.com/watch?v=6ML50I0mVHY')

no_country_for_old_men = movie.Movie('No country For Old Men',
                                     'Bizzare',
                                     'http://orig11.deviantart.net/cb64/f/2013/140/8/0/ncfom2_by_deimos_remus-d65zjnp.jpg',
                                     'https://www.youtube.com/watch?v=38A__WT3-o0')

gone_baby_gone = movie.Movie('Gone baby gone',
                             'girl gets kidnapped,whodunnit?',
                             'https://i.jeded.com/i/gone-baby-gone.29637.jpg',
                             'https://www.youtube.com/watch?v=itPTyd3DkEw')

movies = [shutter_island,the_secret_in_thier_eyes,life_of_david_gale,the_counsellor,no_country_for_old_men,gone_baby_gone]                             
fresh_tomatoes.open_movies_page(movies)                                    

                             

