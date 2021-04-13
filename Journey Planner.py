import tkinter
from tkinter import *

window = Tk()
window.title("Journey Planner")

def resultWindow():
    finalWindow = Toplevel(window)
    graph = {
        #BAKERLOO
        "Harrow & Wealdstone":{"Kenton":2},
        "Kenton":{"South Kenton":2, "Harrow & Wealdstone":2},
        "South Kenton":{"North Wembley":2, "Kenton":2},
        "North Wembley":{"Wembley Central":2, "South Kenton":2},
        "Wembley Central":{"Stonebridge Park":2, "North Wembley":2},
        "Stonebridge Park":{"Harlesden":2, "Wembley Central":2},
        "Harlesden":{"Willesden Junction":2, "Stonebridge Park":2},
        "Willesden Junction":{"Kensal Green":3, "Harlesden":2},
        "Kensal Green":{"Queen's Park":2, "Willesden Junction":3},
        "Queen's Park":{"Kilburn Park":2, "Kensal Green":2},
        "Kilburn Park":{"Maida Vale":2, "Queen's Park":2},
        "Maida Vale":{"Warwick Avenue":1,"Kilburn Park":2},
        "Warwick Avenue":{"Paddington":2, "Maida Vale":1},
        "Paddington":{"Edgware Road":2, "Warwick Avenue":2, "Bayswater":2, "Royal Oak":2},
        "Edgware Road":{"Marylebone":1, "Paddington":2, "Baker Street":3},
        "Marylebone":{"Baker Street":2, "Edgware Road":1},
        "Baker Street":{"Regent's Park":2, "Marylebone":2, "Edgware Road":3, "Great Portland Street":2, "Bond Street":2, "St. John's Wood":3, "Finchley Road":5},
        "Regent's Park":{"Oxford Circus":2, "Baker Street":2},
        "Oxford Circus":{"Piccadilly Circus":2, "Bond Street":2, "Regent's Park":2, "Tottenham":1, "Warren Street":2, "Green Park":2},
        "Piccadilly Circus":{"Charing Cross":2, "Oxford Circus":2, "Green Park":2, "Leicester Square":1},
        "Charing Cross":{"Embankment":1,"Piccadilly Circus":2, "Leicester Square":1},
        "Embankment":{"Waterloo":2, "Charing Cross":1},
        "Waterloo":{"Lambeth North":2, "Embankment":2, "Southwark":2, "Westminster":2, "Bank":5, "Kennington":3},
        "Lambeth North":{"Elephant & Castle":3, "Waterloo":2},
        "Elephant & Castle":{"Lambeth North":3, "Borough":2, "Kennington":2},
        #Central
        "Epping":{"Theydon Bois":3},
        "Theydon Bois":{"Debden":3, "Epping":3},
        "Debden":{"Loughton":2, "Theydon Bois":3},
        "Loughton":{"Buckhurst Hill":3, "Debden":2},
        "Buckhurst Hill":{"Woodford":2, "Loughton":3},
        "Woodford":{"South Woodford":3, "Buckhurst Hill": 2},
        "South Woodford":{"Snaresbrook":2, "Woodford": 3},
        "Snaresbrook":{"Leytonstone":2, "South Woodford":2},
        "Roding Valley":{"Woodford":4, "Chigwell":3},
        "Chigwell":{"Grange Hill":2, "Roding Valley":3},
        "Grange Hill":{"Hainault":5, "Chigwell":2},
        "Hainault":{"Fairlop":2, "Grange Hill":5},
        "Fairlop":{"Barkingside":2, "Hainault":2},
        "Barkingside":{"Newbury Park":2, "Fairlop":2},
        "Newbury Park":{"Gants Hill":3, "Barkingside":2},
        "Gants Hill":{"Redbridge":2, "Newbury Park":3},
        "Redbridge":{"Wanstead":2, "Gants Hill":2},
        "Wanstead":{"Leytonstone":2, "Redbridge":2},
        "Leytonstone":{"Leyton":2, "Wanstead":2, "Snaresbrook":2},
        "Leyton":{"Stratford":3, "Leytonstone":2},
        "Stratford":{"Mile End":4, "Leyton":3, "West Ham":2},
        "Mile End":{"Bethnal Green":2,"Stratford":4, "Stepney Green":2, "Bow Road":2},
        "Bethnal Green":{"Liverpool Street":3, "Mile End":2},
        "Liverpool Street":{"Bank":2,"Bethnal Green":3, "Moorgate":2, "Aldgate":3, "Aldgate East":3},
        "Bank":{"St. Paul's":2,"Liverpool Street":2, "Waterloo":5, "Moorgate":2, "London Bridge":2},
        "St. Paul's":{"Chancery Lane":2,"Bank":2},
        "Chancery Lane":{"Holborn":1,"St. Paul's":2},
        "Holborn":{"Tottenham":2,"Chancery Lane":1, "Russell Square":2, "Covent Garden":2},
        "Tottenham":{"Oxford Circus":1,"Holborn":2, "Goodge Street":1, "Leicester Square":2},
        "Bond Street":{"Marble Arch":2, "Oxford Circus":2, "Green Park":2, "Baker Street":2},
        "Marble Arch":{"Lancaster Gate":3,"Bond Street":2},
        "Lancaster Gate":{"Queensway":2,"Marble Arch":3},
        "Queensway":{"Notting Hill Gate":2, "Lancaster Gate":2},
        "Notting Hill Gate":{"Holland Park":1,"Queensway":2, "High Street Kensington":2, "Bayswater":2},
        "Holland Park":{"Shepherd's Bush":2,"Notting Hill Gate":1},
        "Shepherd's Bush":{"White City":3, "Holland Park":2},
        "White City":{"East Acton":3,"Shepherd's Bush":3},
        "East Acton":{"North Acton":2, "White City":3},
        "North Acton":{"Hanger Lane": 3, "West Acton":2,"East Acton":2},
        "West Acton":{"Ealing Broadway":3, "North Acton":2},
        "Ealing Broadway":{"West Acton":3, "Ealing Common":5},
        "Hanger Lane":{"Perivale":3,"North Acton":3},
        "Perivale":{"Greenford":2,"Hanger Lane":3},
        "Greenford":{"Northolt":2,"Perivale":2},
        "Northolt":{"South Ruislip":3,"Greenford":2},
        "South Ruislip":{"Ruislip Gardens":2,"Northolt":3},
        "Ruislip Gardens":{"West Ruislip":2,"South Ruislip":2},
        "West Ruislip":{"Ruislip Gardens":2},
        #CIRCLE LINE
        "Bayswater":{"Notting Hill Gate":2, "Paddington":2},
        "High Street Kensington":{"Gloucester Road":3, "Notting Hill Gate":2},
        "Gloucester Road":{"South Kensington":3, "High Street Kensington":3, "Earl's Court":2},
        "South Kensington":{"Sloane Square":2, "Gloucester Road":3, "Knightsbridge":2},
        "Sloane Square":{"Victoria":2, "South Kensington":2},
        "Victoria":{"St. James's Park":2, "Sloane Square":2, "Green Park":2, "Pimlico":2},
        "St. James's Park":{"Westminster":2, "Victoria":2},
        "Westminster":{"Embankment":1, "St. James's Park":2, "Green Park":2, "Waterloo":2},
        "Embankment":{"Temple":2, "Westminster":1},
        "Temple":{"Blackfriars":1, "Embankment":2},
        "Blackfriars":{"Mansion House":2, "Temple":1},
        "Mansion House":{"Cannon Street":2, "Blackfriars":2},
        "Cannon Street":{"Monument":1, "Mansion House":2},
        "Monument":{"Tower Hill":2, "Cannon Street":1},
        "Tower Hill":{"Aldgate":2, "Monument":2, "Aldgate East":3},
        "Aldgate":{"Liverpool Street":3, "Tower Hill":2},
        "Moorgate":{"Barbican":2, "Liverpool Street":2, "Old Street":2, "Bank":2},
        "Barbican":{"Farringdon":1, "Moorgate":2},
        "Farringdon":{"King's Cross St. Pancras":4, "Barbican":1},
        "King's Cross St. Pancras":{"Euston Square":2, "Farringdon":4, "Caledonian Road":4, "Russell Square":2, "Highbury & Islington":3, "Euston":2, "Angel":3},
        "Euston Square":{"Great Portland Street":2, "King's Cross St. Pancras":2},
        "Great Portland Street":{"Baker Street":2, "Euston Square":2},
        "Royal Oak":{"Westbourne Park":2, "Paddington":2},
        "Westbourne Park":{"Ladbroke Grove":2, "Royal Oak":2},
        "Ladbroke Grove":{"Latimer Road":2, "Westbourne Park":2},
        "Latimer Road":{"Wood Lane":2, "Ladbroke Grove":2},
        "Wood Lane":{"Shepherd's Bush Market":2, "Latimer Road":2},
        "Shepherd's Bush Market":{"Goldhawk Road":1, "Wood Lane":2},
        "Goldhawk Road":{"Hammersmith":2, "Shepherd's Bush Market":1},
        #DISTRICT LINE
        "Upminster":{"Upminster Bridge":2},
        "Upminster Bridge":{"Hornchurch":2, "Upminster":2},
        "Hornchurch":{"Elm Park":2, "Upminster Bridge":2},
        "Elm Park":{"Dagenham East":3, "Hornchurch":2},
        "Dagenham East":{"Dagenham Heathway":2, "Elm Park":3},
        "Dagenham Heathway":{"Becontree":3, "Dagenham East":2},
        "Becontree":{"Upney":2, "Dagenham Heathway":3},
        "Upney":{"Barking":3, "Becontree":2},
        "Barking":{"East Ham":4, "Upney":3},
        "East Ham":{"Upton Park":2, "Barking":4},
        "Upton Park":{"Plaistow":2, "East Ham":2},
        "Plaistow":{"West Ham":2, "Upton Park":2},
        "West Ham":{"Bromley-by-Bow":2, "Plaistow":2, "Stratford":2, "Canning Town":3},
        "Bromley-by-Bow":{"Bow Road":2, "West Ham":2},
        "Bow Road":{"Mile End":2, "Bromley-by-Bow":2},
        "Stepney Green":{"Whitechapel":3, "Mile End":2},
        "Whitechapel":{"Aldgate East":2, "Stepney Green":3},
        "Aldgate East":{"Tower Hill":3, "Whitechapel":2, "Liverpool Street":3},
        "Earl's Court":{"Kensington (Olympia)":3, "High Street Kensington":5, "West Brompton":2, "West Kensington":2, "Gloucester Road":2, "Barons Court":3},
        "Kensington (Olympia)":{"Earl's Court":3},
        "West Brompton":{"Fulham Broadway":2, "Earl's Court":2},
        "Fulham Broadway":{"Parsons Green":2, "West Brompton":2},
        "Parsons Green":{"Putney Bridge":3, "Fulham Broadway":2},
        "Putney Bridge":{"East Putney":3, "Parsons Green":3},
        "East Putney":{"Southfields":2, "Putney Bridge":3},
        "Southfields":{"Wimbledon Park":2, "East Putney":2},
        "Wimbledon Park":{"Wimbledon":4, "Southfields":2},
        "Wimbledon":{"Wimbledon Park":4},
        "West Kensington":{"Barons Court":2, "Earl's Court":2},
        "Barons Court":{"Hammersmith":3, "West Kensington":2, "Earl's Court":3},
        "Hammersmith":{"Ravenscourt Park":2, "Barons Court":3, "Goldhawk Road":2, "Turnham Green":4, "Acton Town":8},
        "Ravenscourt Park":{"Stamford Brook":2, "Hammersmith":2},
        "Stamford Brook":{"Turnham Green":1, "Ravenscourt Park":2},
        "Turnham Green":{"Gunnersbury":3, "Chiswick Park":2, "Stamford Brook":1, "Hammersmith":4, "Acton Town":4},
        "Gunnersbury":{"Kew Gardens":2, "Turnham Green":3},
        "Kew Gardens":{"Richmond":4, "Gunnersbury":2},
        "Richmond":{"Kew Gardens":4},
        "Chiswick Park":{"Acton Town":2, "Turnham Green":2},
        "Acton Town":{"Ealing Common":2, "Chiswick Park":2, "Hammersmith":8, "Turnham Green":4, "South Ealing":3},
        "Ealing Common":{"Ealing Broadway":5, "Acton Town":2, "North Ealing":2},
        #HAMMERSMITH & CITY LINE
        #JUBILEE
        "Stanmore":{"Canons Park":4},
        "Canons Park":{"Queensbury":3, "Stanmore":4},
        "Queensbury":{"Kingsbury":2, "Canons Park":3},
        "Kingsbury":{"Wembley Park":3, "Queensbury":2},
        "Wembley Park":{"Neasden":4, "Kingsbury":3, "Harrow-on-the-Hill":9, "Finchley Road":7},
        "Neasden":{"Dollis Hill":2, "Wembley Park":4},
        "Dollis Hill":{"Willesden Green":2, "Neasden":2},
        "Willesden Green":{"Kilburn":2, "Dollis Hill":2},
        "Kilburn":{"West Hampstead":2, "Willesden Green":2},
        "West Hampstead":{"Finchley Road":1, "Kilburn":2},
        "Finchley Road":{"Swiss Cottage":2, "West Hampstead":1, "Harrow-on-the-Hill":16, "Wembley Park":7, "Baker Street":5},
        "Swiss Cottage":{"St. John's Wood":2, "Finchley Road":2},
        "St. John's Wood":{"Baker Street":3, "Swiss Cottage":2},
        "Green Park":{"Westminster":2, "Bond Street":2, "Piccadilly Circus":2, "Hyde Park Corner":2, "Oxford Circus":2, "Victoria":2},
        "Southwark":{"London Bridge":2, "Waterloo":2},
        "London Bridge":{"Bermondsey":2, "Southwark":2, "Bank":2, "Borough":2},
        "Bermondsey":{"Canada Water":2, "London Bridge":2},
        "Canada Water":{"Canary Wharf":3, "Bermondsey":2},
        "Canary Wharf":{"North Greenwich":3, "Canada Water":3},
        "North Greenwich":{"Canning Town":3, "Canary Wharf":3},
        "Canning Town":{"West Ham":3, "North Greenwich":3},
        #Metropolitan
        "Amersham":{"Chalfont & Latimer":4},
        "Chesham":{"Chalfont & Latimer":9},
        "Chalfont & Latimer":{"Chorleywood":4, "Chesham":9, "Amersham":4},
        "Chorleywood":{"Rickmansworth":4, "Chalfont & Latimer":4},
        "Rickmansworth":{"Moor Park":5, "Chorleywood":4},
        "Watford":{"Croxley":4},
        "Croxley":{"Moor Park":4, "Watford":4},
        "Uxbridge":{"Hillingdon":4},
        "Hillingdon":{"Ickenham":2, "Uxbridge":4},
        "Ickenham":{"Ruislip":2, "Hillingdon":2},
        "Ruislip":{"Ruislip Manor":2, "Ickenham":2},
        "Ruislip Manor":{"Eastcote":2, "Ruislip":2},
        "Eastcote":{"Rayners Lane":2, "Ruislip Manor":2},
        "Rayners Lane":{"West Harrow":3, "Eastcote":2, "South Harrow":5},
        "West Harrow":{"Harrow-on-the-Hill":2, "Rayners Lane":3},
        "North Harrow":{"Pinner":2, "Harrow-on-the-Hill":3},
        "Pinner":{"Northwood Hills":3, "North Harrow":2},
        "Northwood Hills":{"Northwood":3, "Pinner":3},
        "Northwood":{"Moor Park":3, "Northwood Hills":3},
        "Moor Park":{"Harrow-on-the-Hill":14, "Northwood":3, "Croxley":4, "Rickmansworth":5},
        "Harrow-on-the-Hill":{"Finchley Road":16, "Wembley Park":9, "Northwick Park":3, "Moor Park":14, "North Harrow":3, "West Harrow":2},
        "Northwick Park":{"Preston Road":3, "Harrow-on-the-Hill":3},
        "Preston Road":{"Wembley Park":3, "Northwick Park":3},

        "Cockfosters":{"Oakwood":2},
        "Oakwood":{"Cockfosters":2, "Southgate":3},
        "Southgate":{"Oakwood":3, "Arnos Grove":4},
        "Arnos Grove":{"Southgate":4, "Bounds Green":2},
        "Bounds Green":{"Arnos Grove":2, "Wood Green":3},
        "Wood Green":{"Bounds Green":3, "Turnpike Lane":2},
        "Turnpike Lane":{"Wood Green":2, "Manor House":4},
        "Manor House":{"Turnpike Lane":4, "Finsbury Park":2},
        "Finsbury Park":{"Manor House":2, "Arsenal":1, "Seven Sisters":5, "Highbury & Islington":2},
        "Arsenal":{"Finsbury Park":1, "Holloway Road":2},
        "Holloway Road":{"Arsenal":2, "Caledonian Road":2},
        "Caledonian Road":{"Holloway Road":2, "King's Cross St. Pancras":4},
        "Russell Square":{"King's Cross St. Pancras":2, "Holborn":2},
        "Covent Garden":{"Holborn":2, "Leicester Square":1},
        "Leicester Square":{"Covent Garden":1, "Piccadilly Circus":1, "Tottenham":2, "Charing Cross":1},
        "Hyde Park Corner":{"Green Park":2, "Knightsbridge":2},
        "Knightsbridge":{"Hyde Park Corner":2, "South Kensington":2},
        "South Ealing":{"Acton Town":3, "Northfields":1},
        "Northfields":{"South Ealing":1, "Boston Manor":2},
        "Boston Manor":{"Northfields":2, "Osterley":3},
        "Osterley":{"Boston Manor":3, "Hounslow East":2},
        "Hounslow East":{"Osterley":2, "Hounslow Central":1},
        "Hounslow Central":{"Hounslow East":1, "Hounslow West":3},
        "Hounslow West":{"Hounslow Central":3, "Hatton Cross":4},
        "Hatton Cross":{"Hounslow West":4, "Heathrow Terminals 1, 2, 3":4, "Heathrow Terminal 4":3},
        "Heathrow Terminals 1, 2, 3":{"Hatton Cross":4, "Heathrow Terminal 5":4},
        "Heathrow Terminal 5":{"Heathrow Terminals 1, 2, 3":4},
        "Heathrow Terminal 4":{"Hatton Cross":3},
        "North Ealing":{"Ealing Common":2, "Park Royal":2},
        "Park Royal":{"North Ealing":2, "Alperton":2},
        "Alperton":{"Park Royal":2, "Sudbury Town":3},
        "Sudbury Town":{"Alperton":3, "Sudbury Hill":3},
        "Sudbury Hill":{"Sudbury Town":3, "South Harrow":3},
        "South Harrow":{"Sudbury Hill":3, "Rayners Lane":5},

        "Walthamstow Central":{"Blackhorse Road":3},
        "Blackhorse Road":{"Walthamstow Central":3, "Tottenham Hale":3},
        "Tottenham Hale":{"Blackhorse Road":3, "Seven Sisters":2},
        "Seven Sisters":{"Tottenham Hale":2, "Finsbury Park":5},
        "Highbury & Islington":{"Finsbury Park":2, "King's Cross St. Pancras":3},
        "Euston":{"King's Cross St. Pancras":2, "Warren Street":2, "Mornington Crescent":2, "Camden Town":4},
        "Warren Street":{"Euston":2, "Oxford Circus":2, "Goodge Street":2},
        "Pimlico":{"Victoria":2, "Vauxhall":2},
        "Vauxhall":{"Pimlico":2, "Stockwell":3},
        "Stockwell":{"Vauxhall":3, "Brixton":2, "Oval":2, "Clapham North":2},
        "Brixton":{"Stockwell":2},

        "High Barnet":{"Totteridge & Whetstone":4},
        "Totteridge & Whetstone":{"High Barnet":4, "Woodside Park":2},
        "Woodside Park":{"Totteridge & Whetstone":2, "West Finchley":2},
        "West Finchley":{"Woodside Park":2, "Finchley Central":2},
        "Mill Hill East":{"Finchley Central":4},
        "Finchley Central":{"West Finchley":2, "Mill Hill East":4, "East Finchley":4},
        "East Finchley":{"Finchley Central":4, "Highgate":3},
        "Highgate":{"East Finchley":3, "Archway":3},
        "Archway":{"Highgate":3, "Tufnell Park":2},
        "Tufnell Park":{"Archway":2, "Kentish Town":1},
        "Kentish Town":{"Tufnell Park":1, "Camden Town":2},
        "Edgware":{"Burnt Oak":4},
        "Burnt Oak":{"Edgware":4, "Colindale":2},
        "Colindale":{"Burnt Oak":2, "Hendon Central":3},
        "Hendon Central":{"Colindale":3, "Brent Cross":2},
        "Brent Cross":{"Hendon Central":2, "Golders Green":3},
        "Golders Green":{"Brent Cross":3, "Hampstead":4},
        "Hampstead":{"Golders Green":4, "Belsize Park":3},
        "Belsize Park":{"Hampstead":3, "Chalk Farm":2},
        "Chalk Farm":{"Belsize Park":2, "Camden Town":1},
        "Camden Town":{"Kentish Town":2, "Chalk Farm":1, "Mornington Crescent":2, "Euston":4},
        "Mornington Crescent":{"Camden Town":2, "Euston":2},
        "Goodge Street":{"Warren Street":2, "Tottenham":1},
        "Angel":{"King's Cross St. Pancras":3, "Old Street":3},
        "Old Street":{"Angel":3, "Moorgate":2},
        "Borough":{"London Bridge":2, "Elephant & Castle":2},
        "Kennington":{"Waterloo":3, "Elephant & Castle":2, "Oval":3},
        "Oval":{"Kennington":3, "Stockwell":2},
        "Clapham North":{"Stockwell":2, "Clapham Common":2},
        "Clapham Common":{"Clapham North":2, "Clapham South":2},
        "Clapham South":{"Clapham Common":2, "Balham":2},
        "Balham":{"Clapham South":2, "Tooting Bec":2},
        "Tooting Bec":{"Balham":2, "Tooting Broadway":2},
        "Tooting Broadway":{"Tooting Bec":2, "Colliers Wood":2},
        "Colliers Wood":{"Tooting Broadway":2, "South Wimbledon":2},
        "South Wimbledon":{"Colliers Wood":2, "Morden":3},
        "Morden":{"South Wimbledon":3},


    }

    def dijkstra(graph,start,goal):

        with open("stations.txt", "r") as f:
            stationfile = f.read().split(", ")
    
        Sdistance = {}
        Tprevious = {}
        newNodes = graph
        infinity = 999999
        track_path = []

        for node in newNodes:
            Sdistance[node] = infinity
        Sdistance[start] = 0

        while newNodes:
            mdNode = None
            for node in newNodes:
                if mdNode is None:
                    mdNode = node
                elif Sdistance[node] < Sdistance[mdNode]:
                    mdNode = node
            path_options = graph[mdNode].items()
            for child_node, weight in path_options:
                if weight + Sdistance[mdNode] < Sdistance[child_node]:
                    Sdistance[child_node] = weight + Sdistance[mdNode]
                    Tprevious[child_node] = mdNode
            newNodes.pop(mdNode)
        cNode = goal
        while cNode != start:
            try:
                track_path.insert(0, cNode)
                cNode = Tprevious[cNode]
            except KeyError:
                print("Path is not reachable ")
                break
        track_path.insert(0,start)
        if Sdistance[goal] != infinity:
            Label(finalWindow, text="Shortest Distance Is " + str(Sdistance[goal]) + " minutes\n").pack()
            print("Shortest Distance Is " + str(Sdistance[goal]) + " minutes")
            Label(finalWindow, text="Optimal Path is:\n").pack()
            print("Optimal Path is:")

            CurrentS = 0
            NextS = 1
            Cline = 0
            Nline = 0

            ClineS = []
            NlineS = []

            print(track_path)

            for i in track_path: #repeats for each station in tracked route
                if i == track_path[-1]:
                    print("(", PMlineS, ")", i)
                    Label(finalWindow, text=" ( " + PMlineS + " ) " + i).pack()
                    break

                while track_path[CurrentS] != stationfile[Cline]:
                    Cline += 1
                while track_path[NextS] != stationfile[Nline]:
                    Nline += 1
                Cline += 1
                Nline += 1
                
                while stationfile[Cline] == 'Bakerloo' or stationfile[Cline] == 'Central' or stationfile[Cline] == 'Circle' or stationfile[Cline] == 'District' or stationfile[Cline] == 'Jubilee' or stationfile[Cline] == 'Metropolitan' or stationfile[Cline] == 'Piccadilly' or stationfile[Cline] == 'Victoria Line' or stationfile[Cline] == 'Waterloo & City' or stationfile[Cline] == 'Northern':
                    ClineS.append(stationfile[Cline])
                    print(stationfile[Cline])
                    Cline += 1
                    
                    print(ClineS, 1)
                while stationfile[Nline] == 'Bakerloo' or stationfile[Nline] == 'Central' or stationfile[Nline] == 'Circle' or stationfile[Nline] == 'District' or stationfile[Nline] == 'Jubilee' or stationfile[Nline] == 'Metropolitan' or stationfile[Nline] == 'Piccadilly' or stationfile[Nline] == 'Victoria Line' or stationfile[Nline] == 'Waterloo & City' or stationfile[Nline] == 'Northern':
                    NlineS.append(stationfile[Nline])
                    Nline += 1
                    print(NlineS, 2)
                MlineS1 = set(ClineS) & set(NlineS)
                MlineS = " or ".join(MlineS1)
                if i == track_path[0]:
                    PMlineS = MlineS
                if PMlineS != MlineS:
                    Label(finalWindow, text="(" + PMlineS + ")" + i).pack()
                    Label(finalWindow, text="<Change to " + MlineS + ">").pack()
                    print("(", PMlineS, ")", i)
                    print("<Change to ", MlineS, ">")
                Label(finalWindow, text="(" + MlineS + ")" + i).pack()
                print("(", MlineS, ")", i)
                PMlineS = MlineS
                Cline = 0
                Nline = 0
                CurrentS += 1
                NextS += 1
                ClineS = []
                NlineS = []
                MlineS = []
    dijkstra(graph, StartStation.get(), Destination.get())

label1 = Label(window, text="Enter Starting Station")
label1.pack()

global StartStation
StartStation = Entry(window)
StartStation.pack()

label2 = Label(window, text="Enter Destination")
label2.pack()

global Destination
Destination = Entry(window)
Destination.pack()

button1 = Button(window, text="Calculate", command=resultWindow)
button1.pack()

button2 = Button(window, text="Exit", command=exit)
button2.pack()
            

window.mainloop()