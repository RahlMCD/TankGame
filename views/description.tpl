<table>
  <thead>
    <tr>
      <th><span>Panzer Defensive Stats</span></th>
    </tr>
  </thead>
  <tbody>
    {% for i in results %}
    <tr>
      <td>
       <span>{{user['hash']}} - {{user['name']}}</span>
      </td>
    </tr>
    {% endfor %}
   </tbody>
</table>

<table>
  <thead>
    <tr>
      <th><span>T34 Defensive Stats</span></th>
    </tr>
  </thead>
  <tbody>
    {% for col in rows %}
    <tr>
      <td>{{col}}</td>
    </tr>
    {% endfor %}
   </tbody>
</table>