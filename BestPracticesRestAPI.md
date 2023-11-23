# Best Practices REST API

## Versionierung
`.../vmajorVersion/...` z.B. ``.../v1/...`
- Major: Vorhandene Interaktionen werden verändert (Breaking Changes) (Alte Versionen weiterhin zur Verfügung stellen!)
- Minor: Neue Interaktionen werden hinzugefügt (keine Angabe im Pfad)
- Patch: Fehlerbehebung (keine Angabe im Pfad)

## Allgemeine Tipps für eine gute API

Wenn du eine RESTful API erstellst, ist es wichtig, einige bewährte Praktiken zu beachten, um sicherzustellen, dass sie gut funktioniert und für Entwickler leicht verständlich ist. Hier sind einige Dinge, die du beachten solltest:

1.  **Richtige Verwendung von HTTP-Methoden:**
    
    -   Denk daran, dass verschiedene Aktionen verschiedene HTTP-Methoden erfordern. Zum Beispiel, benutze "GET" für das Abrufen von Daten, "POST" für das Hinzufügen neuer Daten, "PUT" für Aktualisierungen und "DELETE" für das Löschen.
2.  **Klare und eindeutige Adressen (URIs):**
    
    -   Die Adressen sollten leicht verständlich sein. Vermeide es, komplizierte Hierarchien zu erstellen. Nutze klare Substantive für Ressourcen. Zum Beispiel, benutze `GET /users` statt `GET /get_all_users`.
3.  **Verwendung der richtigen HTTP-Statuscodes:**
    
    -   Die Antwort sollte den Erfolg oder das Scheitern der Anfrage klar anzeigen. Zum Beispiel, "200 OK" für Erfolg, "404 Not Found" für nicht gefundene Ressourcen, usw.
4.  **Filtermöglichkeiten für Ressourcen:**
    
    -   Erlaube es Benutzern, Daten mit Filtern zu durchsuchen, damit sie nur die Informationen erhalten, die sie wirklich brauchen.
5.  **Konsistente Endpunkt-Namensgebung:**
    
    -   Halte die Namensgebung deiner Endpunkte einheitlich, damit sie leicht verständlich sind.
6.  **Versionierung:**
    
    -   Wenn du Änderungen an deiner API machst, füge eine Versionsnummer in die Adresse oder den Header ein, um sicherzustellen, dass bestehende Anwendungen weiterhin funktionieren.
7.  **Sicherheit im Blick behalten:**
    
    -   Implementiere Sicherheitsmaßnahmen wie OAuth, um den Zugriff zu kontrollieren. Verwende HTTPS, um die Datenübertragung zu schützen.
8.  **Gute Dokumentation:**
    
    -   Erstelle klare und leicht verständliche Dokumentationen für deine API. Erkläre Ressourcen, Endpunkte, Parameter und gebe Beispiele an.
9.  **Caching nutzen:**
    
    -   Verbessere die Leistung und reduziere die Serverlast, indem du HTTP-Caching-Header verwendest.
10.  **Fehlermeldungen klar gestalten:**
    
    -   Stelle sicher, dass Fehlermeldungen für Entwickler leicht verständlich sind, um Probleme schnell zu diagnostizieren.
11.  **Umfassende Tests durchführen:**
    
    -   Teste deine API gründlich, um sicherzustellen, dass sie wie erwartet funktioniert.
12.  **Rate Limiting implementieren:**
    
    -   Begrenze die Anzahl der Anfragen pro Zeiteinheit, um Missbrauch zu verhindern.

## Versionierung

1.  **Versionierung in der URL:**
    
    -   Füge die Versionsnummer direkt in die URL ein, damit Entwickler leicht erkennen können, welche Version sie verwenden.
2.  **Versionierung im Header:**
    
    -   Gib die gewünschte API-Version im Header an, um eine klare Trennung zwischen Version und Ressource zu haben.
3.  **Versionierung per Anfrageparameter:**
    
    -   Füge die Versionsnummer als Parameter in der URL hinzu, um die gewünschte Version zu identifizieren.
4.  **Semantische Versionierung:**
    
    -   Verwende semantische Versionierung, um anzuzeigen, ob Änderungen rückwärtskompatibel sind.
5.  **Standardversion festlegen:**
    
    -   Definiere eine Standardversion für Benutzer, die keine Version angeben, um eine reibungslose Migration für bestehende Clients zu ermöglichen.

## Namenskonventionen

1.  **Klare und aussagekräftige Ressourcennamen:**
    
    -   Verwende Namen, die den Zweck der Ressource klar widerspiegeln.
2.  **Nutzung von Substantiven:**
    
    -   Verwende Substantive für Ressourcennamen, um die Bedeutung klar zu machen.
3.  **Pluralformen für Ressourcennamen:**
    
    -   Nutze Pluralformen, um die Konsistenz zu wahren.
4.  **Vermeidung von Verben in Ressourcen-URLs:**
    
    -   Lass die HTTP-Methoden die Aktionen angeben. Verwende zum Beispiel `POST /users` statt `POST /createUser`.
5.  **Konsistente Namensgebung für Endpunkte:**
    
    -   Halte die Namensgebung deiner Endpunkte einheitlich für eine leicht verständliche API.
6.  **Verwendung von Bindestrichen für mehrere Wörter:**
    
    -   Trenne Wörter mit Bindestrichen oder Unterstrichen, um die Lesbarkeit zu verbessern. Zum Beispiel, `user-profiles` oder `user_profiles`.

Quelle: ChatGPT, eigen wissen,
https://www.xmatters.com/blog/blog-four-rest-api-versioning-strategies
https://restfulapi.net/resource-naming/
https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/
